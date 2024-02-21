import socket

# addres = input("[+]enter your domin name> ")
ip = socket.gethostbyname("hbh.sh")
print("your terget ip address: "+ip)

#createa a socket boject


for port in range(80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    detles = s.connect_ex((ip, port))
    if detles==0:
        print(port)
    else:
        print("port in use!> "+str(port))
  
    s.close()





