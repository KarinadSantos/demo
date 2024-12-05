import time

hora = 0 
while True:
    print(hora)
    time.sleep(3_600)
    hora = (hora + 1)%24
   