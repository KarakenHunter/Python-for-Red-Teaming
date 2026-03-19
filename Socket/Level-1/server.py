import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 9821)) # .bind() function reserves that port for you on the network.
server.listen(1) # No of connections to accept.
print("Waiting for connections...")

client,addr=server.accept()
# .accept() function returns two values: one is the private socket for that particular client and the other is it's address.
print(f"Connected to {addr}")

data=client.recv(1024) #recv/send function for receiving/sending data and the recv function fetches the X number of bytes in one call.
print(f"Received: {data.decode()}")
client.send("Hello from myside".encode())