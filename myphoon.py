import socket

host = '127.0.0.1'
post = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, post))
s.listen(2)
clientObject, info = s.accept()
print('Cannect to: ',info)

stat = True
while stat:
    res = clientObject.recv(1024)
    print(res.decode())
    if len(res) == 0:
        stat = False
        s.close()
        


