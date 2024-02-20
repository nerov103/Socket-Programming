import socket

domin = input(">")
ip_address = socket.gethostbyname(domin)
print(ip_address)
