import socket


s = socket.socket()
s.bind(('localhost', 5545))
s.listen(4)
clientobjcet, add = s.accept()
# print("server is ready to accet connection")
print("connected with this address", add)
# getdata = clientobjcet.recv(1024)
# getdata.decode('utf-8')
# print(getdata)
# # s.close()

conn = True
while conn:
    getdata = clientobjcet.recv(1024)
    getdata.decode('utf-8')
    print(getdata)
    if len(getdata) ==0:
        conn = False
        s.close()
      





