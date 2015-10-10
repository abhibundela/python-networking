#udp client

import socket

target_host = "127.0.0.1" #loopback address

target_port = 80

# create a socket object

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data no need to connect,udp is connectionless

client.sendto("hello server",(target_host,target_port))

#receive some data

data,addr = client.recvfrom(4096)

print data
