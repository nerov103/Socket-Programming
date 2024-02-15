import socket

tergat_url = "example.com"

request = f"GET / HTTP/1.1\r\nHost: {tergat_url}\n\r\n\r"

ip = socket.gethostbyname(tergat_url)
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

client.send(request.encode())

result = client.recv(10240)

print(result.decode())




