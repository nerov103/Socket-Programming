import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 8080       # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
client_object, _ = s.accept()

# print(client_object)

while True:
    send_data = client_object.makefile("wb")
    send_data.write("Hello World!".encode())
    s.send(send_data)
    send_data.flush()


