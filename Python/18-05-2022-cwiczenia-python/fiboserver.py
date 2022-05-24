def Fibbo(start, end):
    a, b, n = 0, 1, 0
    while True:
        if n in range(start, end):
            if n == end - 1:
                yield a
            else:
                yield a
                yield b
            a, b = b, a + b
        if n == end:
            break
        else:
            a, b = b, a + b
            n += 1

import socket
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            received = conn.recv(1024).decode()
            if received.count(" ") < 2:
                data = 'TOO FEW ARGS!'
            elif received.count(" ") > 2:
                data = 'TOO MUCH ARGS!'
            elif int(received.split(" ")[1]) > int(received.split(" ")[2]):
                data = 'WRONG ARGS!'
            else:
                if received.split(" ")[0] == 'fibo':
                    firstitem = int(received.split(" ")[1])
                    lastitem = int(received.split(" ")[2])
                    for i in Fibbo(firstitem, lastitem):
                        print(i)
                else:
                    data = 'BAD PHRASE'

            if not received:
                conn.close()
                break
            conn.sendall(data.encode())
################################################