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
   ```

2. **Install the required dependency:**
   ```bash
   pip install -r requirements.txt 
   ```
   *(Note: If you are on Arch Linux, you can also install it system-wide with `sudo pacman -S python-scapy`)*
   *(Note: If requirement.txt is not found or gives an error, put the full address of requiremnent.txt by copying its location)*


## 💻 Usage

Because capturing live network traffic requires special permissions, you must run the script with `sudo` (Linux/macOS) or as Administrator (Windows).

### 1. Capture Packets on the Loopback Interface
The loopback interface (`lo`) captures traffic your own computer generates. This is the safest and easiest way to test the sniffer.

**Terminal 1 (Start the sniffer):**
```bash
sudo python3 sniffer.py -i lo -c 5
```

**Terminal 2 (Generate traffic):**
While the sniffer is running, open a second terminal and ping your own machine:
```bash
ping -c 5 127.0.0.1
```
You will see the ICMP packets appear in the first terminal!

### 2. Capture Real Internet Traffic
To see TCP/UDP packets from the internet, listen on the `any` interface and generate web traffic.

**Terminal 1:**
```bash
sudo python3 sniffer.py -i any -c 10
```

**Terminal 2:**
```bash
curl https://example.com
```

### 3. Command-Line Options
| Flag | Description | Example |
| :--- | :--- | :--- |
| `-i` | Network interface to listen on | `-i eth0`, `-i lo`, `-i any` |
| `-c` | Number of packets to capture | `-c 10` (stops after 10 packets) |
| `-h` | Show help message | `python3 sniffer.py -h` |

## 🔍 How It Works

All the logic is contained in a single file (`sniffer.py`) to make it easy to study:

1. **`argparse`**: Handles the command-line arguments you type (like `-i` and `-c`).
2. **`scapy.sniff()`**: The core function that listens to the network interface and waits for packets.
3. **`analyze_packet()`**: A custom function that runs every time a packet is caught. It checks for:
   - **Layer 2**: Ethernet MAC addresses.
   - **Layer 3**: IP addresses (Source and Destination).
   - **Layer 4**: Protocols like TCP, UDP, or ICMP and their ports.
4. **`print()`**: Formats the data into a clean, readable table in your terminal.

## 🛠️ Troubleshooting

- **"Scapy is not installed"**: Make sure you ran `pip install -r requirements.txt` or installed `python-scapy` via your system package manager.
- **"Permission denied"**: You must use `sudo` on Linux/macOS or "Run as Administrator" on Windows to access raw network sockets.
- **"No packets appearing"**: Sniffers only show traffic that is actually happening. If the network is quiet, the sniffer will wait. Try generating traffic with `ping` or `curl` in another window.
- **"Interface not found"**: Try using `-i any` or `-i lo` if you are unsure of your exact network interface name.

   

