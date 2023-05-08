import socket

HOST = "localhost"
PORT = 6379

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.send(b"*1\r\n$4\r\nping\r\n")
    data = s.recv(1024)

