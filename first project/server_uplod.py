import socket
from base64 import b64encode, b64decode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.102", 4001))
s.listen(1)
clientObject, _  = s.accept()


# Function to convert
def listToString(s):
	str1 = ""
	return (str1.join(s))

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
    usr = usr.split(" ")
    if usr[0]=="uplod":
        file_name = listToString(usr[1])
        reciv_text = read_file(file_name)
        usr.append(reciv_text)

    t = listToString(usr[0])
    send_client(b64encode(t.encode()))
    reciv_data()
      

