import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9821))
sock.listen()
print("Waiting for connections...")

client, addr=sock.accept()
print(f"Connected to {addr}")
while True:
    msg=input("~ ")
    client.send(msg.encode('utf-8'))
    data=client.recv(4096)
    print(data.decode('utf-8'))