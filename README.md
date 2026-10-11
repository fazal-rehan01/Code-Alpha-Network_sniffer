# Code-Alpha-Network_sniffer

A simple, easy-to-read network packet sniffer built with Python and Scapy. 
This project is designed for beginners to learn how network packets are structured and how to capture them in real-time.

## 📋 Prerequisites

- **Python 3.8 or newer**
- **Linux, macOS, or Windows**
- **Administrator/root privileges** (required to capture live network traffic)

## 🚀 Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/fazal-rehan01/NetSniffer.git
   cd NetSniffer

💻 Usage
Because capturing live network traffic requires special permissions, you must run the script with sudo (Linux/macOS) or as Administrator (Windows).
1. Capture Packets on the Loopback Interface
The loopback interface (lo) captures traffic your own computer generates. This is the safest and easiest way to test the sniffer.
Terminal 1 (Start the sniffer):
sudo python3 sniffer.py -i lo -c 5

Terminal 2 (Generate traffic):
While the sniffer is running, open a second terminal and ping your own machine:
ping -c 5 127.0.0.1

You will see the ICMP packets appear in the first terminal!
2. Capture Real Internet Traffic
To see TCP/UDP packets from the internet, listen on the any interface and generate web traffic.
Terminal 1:
sudo python3 sniffer.py -i any -c 10

Terminal 2:
curl https://example.com


🔍 How It Works
All the logic is contained in a single file (sniffer.py) to make it easy to study:
argparse: Handles the command-line arguments you type (like -i and -c).
scapy.sniff(): The core function that listens to the network interface and waits for packets.
analyze_packet(): A custom function that runs every time a packet is caught. It checks for:
Layer 2: Ethernet MAC addresses.
Layer 3: IP addresses (Source and Destination).
Layer 4: Protocols like TCP, UDP, or ICMP and their ports.
print(): Formats the data into a clean, readable table in your terminal.
   
