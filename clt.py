import socket

# host = socket.gethostname()
ports = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", ports))
s.send('ima client!'.encode())

msg = s.recv(2048)
print("server said: ", msg.decode())

s.close()

