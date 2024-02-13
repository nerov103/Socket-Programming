import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
s.send("hello ima Client...!".encode())
srv = s.recv(1024)
print("Say server: ",srv.decode())



