import socket
import struct

# create a raw socket using AF_INET family and SOCK_RAW type
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

# set IP_HDRINCL option to include IP header in the packet
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# bind the socket to a network interface
s.bind(("192.168.1.2", 0))

# receive packets
while True:
    # receive packet and its address
    packet, address = s.recvfrom(65535)

    # parse the IP header
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8])
    d_addr = socket.inet_ntoa(iph[9])

    # print some information about the packet
    print(f"Packet from {address[0]} to {d_addr} ({protocol})")

    # do something with the packet
    # ...

# close the socket
s.close()
