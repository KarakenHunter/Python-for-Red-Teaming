import socket
import threading

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9821))
# client, addr=sock.accept()

def send(sock):
    print("Connected!\n")
    while True:
        msg=input("~ ")
        sock.send(msg.encode('utf-8'))

def receive(sock):
    while True:
        response=sock.recv(4096)
        print(response.decode('utf-8'))

t1=threading.Thread(target=receive, args=(sock, ))
t2=threading.Thread(target=send, args=(sock, ))
t1.start()
t2.start()