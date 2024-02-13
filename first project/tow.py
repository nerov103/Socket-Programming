import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.102", 8080))

while True:
    user = input("Say to Server:")
    s.send(user.encode())

    #brack
    if user=="exit":
        s.close()
        break


    