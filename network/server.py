import socket

ip_port = ("0.0.0.0", 3239)
s = socket.socket()
s.bind(ip_port)
print("listening...")
s.listen(2)

conn, addr = s.accept()

print(addr)
conn.close()