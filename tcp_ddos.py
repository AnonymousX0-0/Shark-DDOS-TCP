#!/usr/bin/env python3

import socket

print("|----DDOS-PING----|")
print("|----Anonymous----|")
HOST  = str(input(" IP:"))
PORT = int(input(" PORT:"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)