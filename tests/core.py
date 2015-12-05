import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 89))
sock.send(b"{}")
print(sock.recv(1024))
sock.close()