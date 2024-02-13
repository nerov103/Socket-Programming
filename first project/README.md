
## Title
A socket is a quick connection that allows data to be transmitted between two processes on the same machine or different machines over a network.
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)

# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))




## Documentation


Documentation; Introduction. Version: 4.x. On this page. Introduction. tip. If you are new to Socket.IO, we recommend checking out our tutorial

[Documentation](https://docs.python.org/3/library/socket.html)

[Documentation](https://socket.io/docs/v4/)

## Installation

This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms

![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTCg_jWLVKsq1Pd9EUuVk6AkwBG24zO4P1poCAWxXiyp3QhiXGjkPXrlTDaSXo-puC0Co&usqp=CAU)


## Screenshots

Screenshot 1

![App Screenshot](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)

Screenshot 2

![App Screenshot](https://files.realpython.com/media/Python-Sockets-Tutorial_Watermarked.aebb960a567a.jpg)


Screenshot 3

![App Screenshot](https://www.boardinfinity.com/blog/content/images/2023/04/Copy-of-Maximal-FLow.png)
## Used By

shows how to use socket APIs to establish communication links between remote and local processes.