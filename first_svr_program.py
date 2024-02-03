import socket


s = socket.socket()
s.bind(('localhost', 5545))
s.listen(1)
clientobjcet, add = s.accept()
print("connected with this address", add)

# def send_deta(data):
    	

while True:
    getdata = input(">>")
    clientobjcet.send(getdata.encode())
    


      





