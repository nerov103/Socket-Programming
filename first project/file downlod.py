from socket import socket, AF_INET, SOCK_STREAM

ip = "192.168.0.102"
ports = 8080
soket = socket(AF_INET, SOCK_STREAM)
socket.bind((ip, ports))
socket.listen(1)
client_data, _ = socket.accept()

#main code 


def downlod(name, contand):
    with open(name, "wb") as file:
        file.write(contand)
        return "[+] Downloads Successfull!"



while True:
    user_comd = input("Say client>")
    user_comd = user_comd.split()
    reciv_data = socket.recv(1024)

    if user_comd[0]=="downlod":
        result = downlod(user_comd[1], reciv_data)
    
    print(result)



