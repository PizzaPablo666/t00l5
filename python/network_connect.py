from multiprocessing import connection
import socket

SRV_ADDR = input("Type the server ip address: ")
SRV_PORT = int(input("Type the server port number: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
print("Connection is established! ")

msg = input("Message to send: ")
s.sendall(msg.encode())

s.close()