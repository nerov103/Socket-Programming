from time import time

timeSTART = time()

for i in range(1, 101):
    if i%2==0:
        print("[+]"+str(i))
  

print("code taking time "+str(timeSTART))


