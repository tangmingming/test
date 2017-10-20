import socket

ip_port = ("127.0.0.1", 3239)

s = socket.socket()
s.connect(ip_port)

s.send(bytes("hello"))