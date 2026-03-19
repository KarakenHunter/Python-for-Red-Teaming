import threading

def greet():
    print("Hello guyzzz!")
t=threading.Thread(target=greet) # Creates a thread and assign it to the target
t.start()