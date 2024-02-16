import socket

ip = socket.gethostbyname(socket.gethostname())
port = 8080


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((ip, port))
client.listen(2)
client_object, _ = client.accept()

while True:
    client_object.send(html_code.encode())

    


