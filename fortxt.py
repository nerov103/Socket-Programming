import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.102", 5000))
s.listen(1)
clientObject, detls_for_client_maching = s.accept()
print(detls_for_client_maching)


file_name = str(input("enter your file name:"))
file = open(file_name, "rb")
tx = file.read()
clientObject.send(tx)
print("file send successfull...")






