import threading
import time

def task1():
    while True:
        print("A")
        time.sleep(1)

def task2():
    while True:
        print("B")
        time.sleep(1)

threading.Thread(target=task1).start()
threading.Thread(target=task2).start()