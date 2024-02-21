import socket
import time
from colorama import Fore

#ip address and port number
ip = input("[+]enter your target domin name>")

ip_address = socket.gethostbyname(ip)


#createa a socket object
s = socket.socket()
data = s.connect_ex((ip, 80))
print("port in open "+str(data))





   











