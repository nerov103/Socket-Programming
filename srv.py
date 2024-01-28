import socket

ports = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', ports))
s.listen(1)

clientobject, addr= s.accept()
message = clientobject.recv(1024)
print('Client said: ', message.decode())
clientobject.send("Hello World!".encode())
s.close()














