import socket
from IPy import IP


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scanner(ipaddress1, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ipaddress1, port))
        print('Port ' + str(port) + ' is open')
    except:
        print('Port ' + str(port) + ' is closed')


ipaddress1 = input('Enter the IP address: ')
converted_ip = check_ip(ipaddress1)

for port in range(78, 82):
    scanner(converted_ip, port)
