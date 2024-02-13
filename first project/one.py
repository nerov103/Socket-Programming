import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.102", 8080))
s.listen()
clientObjcet, desl = s.accept()
print("connedact to> ", desl)

while True:
    msg = clientObjcet.recv(1024)
    print(msg.decode())

    #brack
    if len(msg)==0:
        s.close()
        break




