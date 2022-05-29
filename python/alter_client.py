import socket

SRV_ADDR = '192.168.2.250'
SRV_PORT = 6666

def print_menu():
    print("""\nClose connection -> 0
    \n Info about OS -> 1
    \n List Files -> 2\n""")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))

print("Connection established")
print_menu()

while 1:
    msg = input("Select option")

    if(msg == "0"):
        s.sendall(msg.encode())
        s.close()
        break
    elif (msg == '1'):
        s.sendall(msg.encode())
        data = s.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
    elif (msg == '2'):
        path = input('Insert the path: ')
        s.sendall(msg.encode())
        s.sendall(path.encode())
        data = s.recv(1024)
        data = data.decode('utf-8').split(',')
        print("*"*40)
        for x in data:
            print(x)
        print("*"*40)

print_menu()
