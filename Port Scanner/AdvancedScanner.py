import socket
from IPy import IP


def scan(ipaddress):
    converted_ip = check_ip(ipaddress)
    print('\n' + 'scanning target ' + str(ipaddress))
    for port in range(1, 100):
        scanner(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)


def scanner(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))

        try:
            banner = get_banner(sock)
            print('Port ' + str(port) + ' is open: ' + str(banner.decode()))
        except:
            print('Port ' + str(port) + ' is open.')
    except:
        pass


ipaddress = input('Enter the IP addresses ( split multiple targets with , ): ')

if ',' in ipaddress:
    for ip_add in ipaddress.split(','):
        scan(ip_add.strip(' '))
else:
    scan(ipaddress)
