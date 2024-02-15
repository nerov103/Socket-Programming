import socket

def accept():
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)



accept()
