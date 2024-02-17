import time

def main_function():

    def one():
        print("ima one function")
    time.sleep(2)
    def tow():
        print("ima tow function")
    time.sleep(2)
    def three():
        print("ima three function")
    
    one()
    tow()
    three()

while True:
    main_function()





