import threading
import time

done = False


def worker():
    number_count = 0
    while not done:
        number_count +=1
        time.sleep(1)
        print(number_count)
        


thd = threading.Thread(target=worker)
thd.start()



input("press enter quit prgram")
done = True







