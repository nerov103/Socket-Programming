import base64
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.0.102", 5000))

# #create a function this finction use to read a file 
# file_name = input("type your file name:")
# x = open(file_name, "wb")

# file_data = s.recv(1024)
# x.write(file_data)
# x.close()


# print("Successfully received....")


# ex = "This my first love"
# ex = ex.split(" ")
# print(ex)


def readfile():
    file_name = str(input('enter your file name:'))
    with open(file_name, "rb") as f:
        return base64.b64encode(f.read())


result = readfile()
resultx = base64.b64decode(result).decode()

print(type(resultx))
print(resultx)

