import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	name = "Modul_server.pdf"
	print("waiting for a connection")
	connection, client_address = sock.accept()
	print(f"connection from {client_address}")
	# Receive the data in small chunks and retransmit it
	filename = open(f"{name}", 'wb')  # open in binary
	while True:
		# data = connection.recv(32)
		data = connection.recv(1024)
		if not data:
			break
		filename.write(data)
	# Clean up the connection
	filename.close()
	print(f"File Received with name {name}")
	print("\n")
	connection.close()