from time import sleep
from threading import Thread


user_input = str(input("Say Python..|"))
stor = False

def auto_type():
    global stor,user_input
    while not True:
        print(user_input)

Thread(target=auto_type).start()


input("enter")
stor = True


