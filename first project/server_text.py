import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8080))
s.listen(1)
clientobject, systeminfo = s.accept()
data_recev = clientobject.recv(2048)
print("Say Client: ",data_recev.decode())

clientobject.send("Hello ima Server...!".encode())
clientobject.close()




