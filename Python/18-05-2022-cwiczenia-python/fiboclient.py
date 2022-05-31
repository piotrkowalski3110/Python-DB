# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        task = input()
        if len(task) == 0:
            break
        s.sendall(task.encode())
        data = s.recv(1024)
        print('Received', repr(data), "\n")

