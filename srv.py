import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('www.example.com', 80)  # Connect to a web server on port 80
sock.connect(server_address)

# Now you can send and receive data over the connection

