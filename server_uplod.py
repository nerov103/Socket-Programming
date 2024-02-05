import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.102", 4001))
s.listen(1)
clientObject, _  = s.accept()

#createa a file uplod function
def read_file(file_path):
    with open(file_path, "rb") as f:
        return f.read()
    
#reciv data for client
def reciv_data():
    print(clientObject.recv(2048).decode())

#send for cliend
def send_client(data):
    clientObject.send(data)


while True:
    usr = str(input("comand:"))
    usr = usr.split()
    if usr[0]=="uplod":
        reciv_text = read_file([usr[1]])
        usr.append(reciv_text)
        
    reciv_data()
    send_client(usr)    


