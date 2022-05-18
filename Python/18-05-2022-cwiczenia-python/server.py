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

            if received.count(" ") == 1:
                data = 'TOO FEW ARGS!'

            else:
                if received.split(" ")[0] == 'add':
                    result = int(received.split(" ")[1])
                    for n in range(2, received.count(" ") + 1):
                        result += int(received.split(" ")[n])
                    data = str(result)

                elif received.split(" ")[0] == 'substract':
                    result = int(received.split(" ")[1])
                    for n in range(2, received.count(" ") + 1):
                        result -= int(received.split(" ")[n])
                    data = str(result)

                elif received.split(" ")[0] == 'multiply':
                    result = int(received.split(" ")[1])
                    for n in range(2, received.count(" ") + 1):
                        result *= int(received.split(" ")[n])
                    data = str(result)

                elif received.split(" ")[0] == 'divide':
                    result = int(received.split(" ")[1])
                    for n in range(2, received.count(" ") + 1):
                        result /= int(received.split(" ")[n])
                    data = str(result)

                else:
                    data = 'BAD MATH OPERATION!'

            if not received:
                conn.close()
                break
            conn.sendall(data.encode())
