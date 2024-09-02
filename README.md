# ScanMystique - Enhanced Network Scanner 🔍

ScanMystique is a Nmap-based tool to provide advanced network scanning designed to detect network, operating system, and service version information. It provides a user-friendly interface to initiate scans, visualize results, and gain insights into the security of your network.


## Features 🚀

- **Comprehensive Scanning:** ScanMystique uses Nmap to perform detailed scans of target IPs, IP ranges, or URLs.
- **OS Detection:** Detect the operating system running on the scanned hosts.
- **Service Version Identification:** Identify the services and their versions running on open ports.
- **User-Friendly GUI:** Intuitive graphical interface for easy interaction and visualization of scan results.

## Usage 🛠️

### Option 1: Exe File

1. Download the [exe file](https://github.com/ananquay15x9/ScanMystique/blob/v1.0/ScanMystique.exe) from the master branch.
2. Run the executable to launch the ScanMystique tool.

### Option 2: Python Code

1. Download the [Python code](https://github.com/ananquay15x9/ScanMystique/blob/v1.0/ScanMystique.py) from this repository.
2. Open the code in your preferred IDE.
3. Run the code in your IDE.

### Option 3: Git Clone

Alternatively, you can clone the project using Git:

```bash
git clone https://github.com/ananquay15x9/ScanMystique.git
cd ScanMystique
python ScanMystique.py
```

## How to Use 📖

1. **Make sure to have Python3 on your machine**
    - On Windows, visit the [official Python website](https://www.python.org/downloads/).
    - Click "Downloads Python 3.1x.x"
    - Make sure to check "Add Python 3.x to PATH" during installation.
        - On Linux, Python3 varies depending on the distribution.
        - Debian/Ubuntu/Mint:
        - ```bash
          sudo apt update
          sudo apt install python3
          ```
        - Arch:
        - ```bash
            sudo pacman -Syu
            sudo pacman -S python
           ```
        - Fedora:
        - ```bash
            sudo dnf install python3
           ```
          
2. **Make sure to install Nmap to run this tool**
    - On Windows, visit the official Nmap download page [here](https://nmap.org/download.html).
    - Follow the on-screen instructions to install Nmap. Please check to install Ncap during installation.
    - Make sure you add Nmap to the system PATH. Usually, Nmap is located at (C:\Program Files (x86)\Nmap).
    - You can add it manually at "Edit the system environment variables."
    - Find and select the "Path" variable, hit "New" and paste the path to Nmap directory.
    - Click "OK" to close. 
        - On Linux, Nmap varies depending on the distribution.
        - Debian/Ubuntu/Mint:
        - ```bash
            sudo apt update
            sudo apt install nmap
            ```
        - Arch:
        - ```bash
              sudo pacman -Syu
              sudo pacman -S nmap
             ```
         - Fedora:
         - ```bash
              sudo dnf install nmap
             ```
3. **Start Scanning**
    - Input the target IP addresses, IP ranges, or URLs into the provided entry field.
    - Click the "Start Scan" button. The tool will display a comprehensive reoprt including detected operating systems, open ports, and service versions. 

4. **Stay Legal and Ethical:**
    - Ensure that you have the right to scan the specified targets, and always adhere to legal and ethical guidelines. Unauthorized scanning of networks is illegal and unethical.


## Contributing 🤝

Contributions are welcome! Feel free to open issues, suggest enhancements, or submit pull requests to improve the project.

## License 📝

This project is licensed under the [MIT License](LICENSE).

---

**ScanMystique** - Uncover the secrets of your digital landscape and fortify your security. Stay vigilant, stay secure in the interconnected realm ✨

