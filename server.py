import socket

# Redis uses port 6379; we need to bind port 6379 to a TCP Server
HOST = "localhost"
PORT = 6379

# Server respond to ping with pong
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data = b"*1\r\n$4\r\nping\r\n": #Ping looks monstrous due to RESP
                conn.send(b"+PONG\r\n")
                break
