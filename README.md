# ScanMystique - Enhanced Network Scanner 🔍

ScanMystique is a Nmap-based tool to provide advanced network scanning designed to detect network, operating system, and service version information. It provides a user-friendly interface to initiate scans, visualize results, and gain insights into the security of your network.


## Features 🚀

- **Comprehensive Scanning:** ScanMystique uses Nmap to perform detailed scans of target IPs, IP ranges, or URLs.
- **OS Detection:** Detect the operating system running on the scanned hosts.
- **Service Version Identification:** Identify the services and their versions running on open ports.
- **User-Friendly GUI:** Intuitive graphical interface for easy interaction and visualization of scan results.

## Usage 🛠️

### Prerequisites

- Python 3
- Nmap

#### Windows

**Nmap:** Download and install Nmap for Windows from [nmap.org](https://nmap.org/download.html). Ensure that Nmap is added to your system's PATH during installation. During installation, there will be a check box for Ncap to be installed, please check that box. I have realized that VPN will prevent NMAP to work. To use this tool, please turn off VPN. 

**Tkinter:** Tkinter is included with most Python installations on Windows. No additional installation is required.

#### Linux

**Pre-install:**  
#### Debian/Ubuntu/Mint:
  ```bash
  sudo apt update
  sudo apt install python3 #to install python3

```
  ```bash
  sudo apt-get update
  sudo apt-get install nmap #to install nmap
```
  ```bash
 sudo apt-get install python3-tk #to install tkinter
```

#### Arch:
  ```bash
  sudo pacman -Syu  # Update your system
  sudo pacman -S python #to install python

```

  ```bash
  sudo pacman -S nmap #to instsall nmap
```

  ```bash
  sudo pacman -S tk #to install tkinter
```


## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/ananquay15x9/ScanMystique.git
   cd ScanMystique
   ```
   
