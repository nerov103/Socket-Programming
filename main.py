import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# print(socket.gethostbyname("google.com"))
try:
    terget_ipaddres = socket.gethostbyname("goog le.com") #একটি IP ঠিকানা থেকে একটি হোস্টনেম খুঁজে বের করে।
    pot = 80
except socket.gaierror as err:
    print(f"Name or Service not know ", err)


s.connect((terget_ipaddres, pot))

print("connect successfull to goole")






