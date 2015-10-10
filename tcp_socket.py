# Tcp client 

import socket

target_host = "www.google.com"
target_port = 80
 
#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the client never forget to use bracket, connect take one argument

client.connect((target_host,target_port)) 

#send some data

client.send("GET /HTTP/1.1\r\nHOST: google.cm\r\n\r\n")

# recieve some data

response = client.recv(1024) #1024 is size of bytes to recieve

print response


