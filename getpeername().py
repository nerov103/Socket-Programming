import socket

ip = socket.gethostbyname('hackthissite.org')
port = 80

s = socket.socket()
s.connect((ip, port))

# ipaddr, ports = s.getpeername()
ipaddr, ports = s.getsockname()

print(ipaddr)
print(ports)



