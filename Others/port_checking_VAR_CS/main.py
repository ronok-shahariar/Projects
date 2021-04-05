import socket
from IPy import IP

ipaddress = input('[+] Enter target To Scan: ')
port = 80

try:
    sock = socket.socket()
    sock.connect(ipaddress, port)
    print('[+] port 80 is Open')
except:
    print('[-] port 80 is Closed')
