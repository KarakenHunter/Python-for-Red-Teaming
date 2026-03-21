import socket
import threading
import sys

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9821))
print("[*] Waiting for connection...")
sock.listen()
collection = {}

def assignclients():
    while True:
        client, addr = sock.accept()
        collection[f'{addr}'] = f'{client}'
        sys.stdout.write(f"\rConnected clients:\n {collection}")
        sys.stdout.flush()

t1 = threading.Thread(target=assignclients)
t1.daemon = True
t1.start()
while True:
    pass