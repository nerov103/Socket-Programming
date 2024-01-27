import socket


s = socket.socket()
s.connect(('localhost', 5545))

# meassge = "Hello this is first client!"
# s.send(meassge.encode('utf-8'))
# s.close()

conn = True
while conn:
    msg = input('enter your massge:')
    s.send(msg.encode('utf-8'))
    if msg == 'no':
        conn = False
        s.close()
    

