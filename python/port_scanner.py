import socket


target = input("Enter the IP address to scan: ")
port_range = input('Enter a port range to scan (ex. 5-200): ')

low_port = int(port_range.split('-')[0])
high_port = int(port_range.split('-')[1])

print('Scanning host: ', target, 'from port ', low_port, 'to ', high_port)

for port in range(low_port, high_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if (status == 0):
        print('*** Port ', port, ' - OPEN ***')
    else:
        print('Port ', port, ' - CLOSED')

s.close()