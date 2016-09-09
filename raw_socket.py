          #Raw socket is an internet socket that allows direct sending and receiving of Internet Protocol packets without any protocol-specific transport layer formatting.

import socket
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x800)) #PF_Packet for telling the kernel packet interface 

#sock_raw telling the kernel about raw socket and socket.htons(0x800) tells protocol we are interested 0x8000 tells about ip protocol

#linux directory /usr/include/linux/if_ether.h

#We can only use raw_socket only if root user but we can grant non-root user permission to use raw_socket

pkt = rawSocket.recvfrom(2048)

ethernetHeader = pkt[0][0:14]

eth_hdr = struct.unpack("!6s6s2s",ethernetHeader)
binascii.hexlify(eth_hdr[0])
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])
ipHeader = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s",ipHeader)
print "Source IP address " + socket.inet_ntoa(ip_hdr[1])
print "Destination IP address " + socket.inet_ntoa(ip_hdr[2])
