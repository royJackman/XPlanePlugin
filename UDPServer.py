import socket
import time

ip_addr = '127.0.0.1'
port = 49001

addr = (ip_addr, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip_addr, port))

while True:
    data, server = s.recvfrom(1024)
    print(data, server)