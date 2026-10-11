#!/usr/bin/env python3
"""
Beginner-Friendly Network Packet Sniffer
Built with Scapy. Captures packets and prints basic information about them.

Usage:
    sudo python3 sniffer.py -i eth0 -c 5
"""
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="scapy")
import argparse
import sys

# Import only the essential Scapy components
try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP, Ether
except ImportError:
    print("Error: Scapy is not installed. Please run: pip install scapy")
    sys.exit(1)


def analyze_packet(packet):
    """
    Inspects a single packet and prints its basic details.
    This function is called automatically by Scapy for every captured packet.
    """
    # 1. Get the basic length and protocol name
    length = len(packet)
    
    # Check if the packet has an Ethernet layer
    if Ether in packet:
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
    else:
        src_mac = "Unknown"
        dst_mac = "Unknown"

    # 2. Check for Network Layer (IP)
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_num = packet[IP].proto
        
        # Determine the transport protocol based on the IP protocol number
        if TCP in packet:
            proto_name = "TCP"
            ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
        elif UDP in packet:
            proto_name = "UDP"
            ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
        elif ICMP in packet:
            proto_name = "ICMP"
            ports = "N/A (Control Message)"
        else:
            proto_name = f"Other (Proto {protocol_num})"
            ports = "N/A"
            
    else:
        # If it's not an IP packet (e.g., pure ARP), keep it simple
        src_ip = "N/A"
        dst_ip = "N/A"
        proto_name = "Non-IP"
        ports = "N/A"

    # 3. Print the results in a clean, readable format
    print(f"[{length:4} bytes] {proto_name:6} | {src_ip:15} -> {dst_ip:15} | {ports}")


def main():
    # Set up simple command-line arguments
    parser = argparse.ArgumentParser(description="A simple beginner network sniffer.")
    parser.add_argument("-i", "--interface", default="any", help="Network interface to listen on (default: any)")
    parser.add_argument("-c", "--count", type=int, default=5, help="Number of packets to capture (default: 5)")
    
    args = parser.parse_args()

    print(f"Starting capture on interface '{args.interface}' for {args.count} packets...")
    print("-" * 75)
    print(f"{'Size':<8} | {'Proto':<6} | {'Source IP':<15} -> {'Dest IP':<15} | {'Ports / Info'}")
    print("-" * 75)

    try:
        # The core Scapy sniff function
        # prn=analyze_packet tells Scapy to run our function on every packet
        sniff(iface=args.interface, count=args.count, prn=analyze_packet)
        
    except PermissionError:
        print("\nError: Permission denied. You likely need to run this with 'sudo'.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

    print("-" * 75)
    print("Capture complete.")


if __name__ == "__main__":  # Note: Fixed the missing underscores from your original file
    main()