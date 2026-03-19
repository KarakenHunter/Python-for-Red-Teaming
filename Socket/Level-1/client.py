import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9821))

client.send("Hello world".encode())
response=client.recv(4096)
print(f"Server said: {response.decode()}")
