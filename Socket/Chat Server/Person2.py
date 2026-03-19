import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9821))
print("Connected Successfully!")
while True:
    resp=sock.recv(4096)
    print(resp.decode('utf-8'))
    msg=input("~ ")
    sock.send(msg.encode('utf-8'))