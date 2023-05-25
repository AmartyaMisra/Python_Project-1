import os
import sys
import argparse
from scapy.all import ARP, Ether, srp

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target IP or IP range. Use --help for more information.")
    return options

def scan(ip):
    # Create ARP request packet
    arp = ARP(pdst=ip)
    # Create Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine packet and frame
    packet = ether/arp
    # Send packet and receive response
    result = srp(packet, timeout=3, verbose=0)[0]
    # Parse response
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

def print_result(results):
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for client in results:
        print("{:<15}    {}".format(client['ip'], client['mac']))

options = get_arguments()
scan_results = scan(options.target)
print_result(scan_results)