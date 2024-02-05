import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.102", 5000))
s.listen(1)
clientObject, detls_for_client_maching = s.accept()
print(detls_for_client_maching)

#here write new code in image send





print("file send successfull...")

