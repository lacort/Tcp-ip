import threading
import time


def worker(message):
    for i in range(5):
        print(message)
        time.sleep(1)

def worker2(message):
    for i in range(5):
        print(message)
        time.sleep(2)

t = threading.Thread(target=worker, args=("thread sendo executada",))
t.start()


t2 = threading.Thread(target=worker2, args=("thread2 sendo executada",))
t2.start()
while t.isAlive():
    print("Aguardando thread")
    time.sleep(5)

print("Thread morreu")
print("Finalizando programa")