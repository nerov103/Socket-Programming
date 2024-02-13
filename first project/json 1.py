import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.102", 5000))
s.listen(1)
clientObject, detls_for_client_maching = s.accept()
print(detls_for_client_maching)


def send_client(data):
    json_data = json.dumps(data)
    encode_data = json_data.encode("utf-8")
    clientObject.send(encode_data)

def reciv_client():
    json_data = clientObject.recv(1024)
    decode_data = json_data.decode("utf-8")
    return json.loads(decode_data)

def main_function(cmd):
    send_client(cmd)
    return reciv_client()


while True:
    
    user_cmd = input("Say client:")
    reciv_for_client_data = main_function(user_cmd)

    print(type(reciv_for_client_data))








