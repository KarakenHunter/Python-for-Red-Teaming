import socket
import threading

def handle_clients(client_socket):
	while True:
		try:
			data=client_socket.recv(1024)
			if not data:
				break
			print(f"Client: {data.decode()}")
			client_socket.send("Got it!".encode())
		except:
			break
		client_socket.close()

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9821))
server.listen()

while True:
	client, addr=server.accept()
	print(f"Connected to {addr}")
	thread=threading.Thread(target=handle_client, args=(client_socket,))
	thread.start()