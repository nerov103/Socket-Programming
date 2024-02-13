import socket

host = '127.0.0.1'
post = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, post))

stat = True
while stat:
    user_mass = input("Send to Client mas: ")
    s.send(user_mass.encode())
    # mess = s.recv(2048)
    # print("say server[+] ", mess.decode())
    if user_mass=='exit':
        stat = False
        s.close()


