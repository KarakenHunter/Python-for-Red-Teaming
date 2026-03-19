import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9821))
sock.listen()
print("[*] Waiting for connections...")

client, addr=sock.accept()
print(f"Connected to {addr}")
while True:
    command=input("#~ ")
    client.send(command.encode('utf-8'))
    resp=client.recv(4096).decode('utf-8')
    print(resp)
