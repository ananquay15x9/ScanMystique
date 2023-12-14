# -------------------------------------------------------------------------
# ScanMystique
# -------------------------------------------------------------------------
# Description:
#   This Python script is an enhanced network scanner based on the Nmap tool.
#   It detects network, operating system, and service versions of target hosts.
#
# Author:
#   uu2
#
# GitHub Repository:
#   [Link to the GitHub repository]
#
# Date: 12/13/2023
# -------------------------------------------------------------------------




import nmap
import argparse
import ipaddress
from datetime import datetime
import socket
import tkinter as tk
from tkinter import ttk  # Import ttk module for Progressbar
import threading
import platform


def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def resolve_target(target):
    try:
        if is_valid_ip(target):
            return target
        else:
            ip_address = socket.gethostbyname(target)
            return ip_address
    except socket.gaierror:
        print(f"[-] Error: Unable to resolve the IP address for {target}")
        return None

def format_nmap_output(nmap_data):
    formatted_output = ""
    if 'scan' in nmap_data:
        for ip, data in nmap_data['scan'].items():
            formatted_output += f"Nmap scan report for {ip}"

            if 'hostnames' in data and data['hostnames']:
                hostnames = [hostname['name'] for hostname in data['hostnames'] if 'name' in hostname]
                if hostnames:
                    formatted_output += f" ({', '.join(hostnames)})"
                
            formatted_output += "\nHost is up.\n"

            if 'osmatch' in data:
                formatted_output += "\n[+] Detected Operating System (osmatch):\n"
                for osmatch in data['osmatch']:
                    formatted_output += f"  - {osmatch['name']} ({osmatch['accuracy']}%)\n"

                linux_identified = any("Linux" in osmatch['name'] for osmatch in data['osmatch'])
                if not linux_identified:
                    formatted_output += "[+] Can't display OS (Linux not identified).\n"
            else:
                formatted_output += "[+] Can't display OS.\n"

            if 'portused' in data:
                formatted_output += "\nPORT           STATE          SERVICE\n"
                for port in data['portused']:
                    formatted_output += f"{port['portid']}/tcp".ljust(15) + f"{port['state']}".ljust(15) + f"{port['proto']}\n"

                if 'service/version' in data:
                    formatted_output += "\n[+] Service Version Detection:\n"
                    for service in data['service/version']:
                        formatted_output += (
                            f"  - Port {service['port']}/{service['proto']}: "
                            f"{service['name']} ({service['product']} {service['version']})\n"
                        )

    return formatted_output

def format_scan_duration(duration):
    return f"{duration.seconds} seconds"

def run_scan(target, options, output_text, progress_bar):
    try:
        resolved_target = resolve_target(target)

        if resolved_target:
            nm = nmap.PortScanner()
            output_text.insert(tk.END, f"--------------------------------------------------\n")
            output_text.insert(tk.END, f"Starting scan for {resolved_target}\n")
            output_text.update_idletasks()

            start_time = datetime.now()

            if platform.system() == 'Windows':
                scan_args = '-p 1-1024,22,23,25,20,21,53,80,110,119,123,143,161,194,443 -sS -O -A -T4'
            else:
                scan_args = '-p 1-1024,22,23,25,20,21,53,80,110,119,123,143,161,194,443 -sS -O -A -T4 --min-hostgroup 1 --max-hostgroup 1'
                
            nm.scan(hosts=resolved_target, arguments=scan_args)

            end_time = datetime.now()
            scan_duration = end_time - start_time
            formatted_duration = format_scan_duration(scan_duration)
            output_text.insert(tk.END, f"\n[SCAN DURATION] Scan completed for {resolved_target} in {formatted_duration}\n")
            output_text.update_idletasks()

            nmap_output = nm._scan_result
            formatted_output = format_nmap_output(nmap_output)

            output_text.insert(tk.END, f"[INFO] nmap output for {resolved_target}:\n{formatted_output}\n")
            output_text.update_idletasks()

    except nmap.PortScannerError as e:
        output_text.insert(tk.END, f"[-] An error occurred while scanning {target}: {e}\n")
    except Exception as e:
        output_text.insert(tk.END, f"[-] An unexpected error occurred: {e}\n")
    finally:
        progress_bar.stop()  # Stop the indeterminate progress bar

def main():
    root = tk.Tk()
    root.title("ScanMystique")

    targets_label = tk.Label(root, text="Enter target IPs, IP ranges, or URLs separated by commas:")
    targets_label.pack()

    targets_entry = tk.Entry(root)
    targets_entry.pack()

    description_label = tk.Label(root, text="This tool detects network, OS, and service version.")
    description_label.pack()

    output_text = tk.Text(root, height=10, width=50)
    output_text.pack()

    progress_bar = ttk.Progressbar(root, mode='indeterminate', length=100)
    progress_bar.pack()

    def on_scan_button_click():
        progress_bar.start(10)  # Start the indeterminate progress bar
        threading.Thread(target=run_scan, args=(targets_entry.get(), None, output_text, progress_bar)).start()

    scan_button = tk.Button(root, text="Start Scan", command=on_scan_button_click)
    scan_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
