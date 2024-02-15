import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("www.hackthissite.org", 80))

sock.send(b"GET / HTTP/1.1\r\nwww.hackthissite.org\r\n\r\n")
response = sock.recv(4096)
sock.close()
print(response.decode())







