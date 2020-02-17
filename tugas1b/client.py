import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

Filename = "CheeseCake.jpg"
filetok, file_extension = os.path.splitext(Filename)
sock.send(Filename.encode('utf-8'))
sock.shutdown(socket.SHUT_WR)

clientName = "CheeseCake_client.jpg"
f = open(f"{clientName}", 'wb')  # open in binary
data = sock.recv(1024)
while(data):
    f.write(data)
    data = sock.recv(1024)
print(f"File received with filename {clientName}")
print("closing")
f.close()
sock.close()