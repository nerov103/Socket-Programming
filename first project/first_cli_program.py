import socket
import json

s = socket.socket()
s.connect(('localhost', 5545))

def reciv():
    reciv_data =  s.recv(1024).decode()
    return reciv_data.split()
    


        
while  True:
    reciv_command = reciv()
    print(type(reciv_command)) #print the reciv deta type
    print(reciv_command) #print reciv deta
    print(len(reciv_command)) #len of reciv data 
    print(reciv_command[0])
    print(reciv_command[1])


#Now ami show who is data pass in python socket programming send method ....





