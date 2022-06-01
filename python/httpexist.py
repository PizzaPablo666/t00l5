import http.client

print("** This program returns 'exist' if the specific resource exists **\n")

host = input("Insert the host/IP: ")
port = int(input("Insert the port (default:80): "))
resource = input("Insert the resource you want to GET")

if (port == ""):
    port = 80
    
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', resource)
    response = connection.getresponse()
    print("Status = ", response.status)
    if (response.status == 200):
        print("** EXISTS **")
    elif (response.status == 302 or response.status == 301):
        print('** REDIRECTED **')
    else:
        print("Doesn't exist")
    connection.close()
except ConnectionRefusedError:
    print('Connection failed!')