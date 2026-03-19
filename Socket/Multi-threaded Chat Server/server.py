import socket
import threading

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9821))
sock.listen()
client, addr=sock.accept()

def send(sock):
    print("Connected!")
    while True:
        msg=input("~ ")
        sock.send(msg.encode('utf-8'))

def receive(sock):
    while True:
        response=sock.recv(4096)
        print(response.decode('utf-8'))

t1=threading.Thread(target=receive, args=(client, ))
t2=threading.Thread(target=send, args=(client, ))
t1.start()
t2.start()