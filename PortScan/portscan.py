import sys
import socket

ip = sys.argv[1]
ports = range(1, 10000)

for port in ports:
    sock = socket.socket()
    ret = sock.connect_ex((ip, port))

    if ret == 0:
        print("{} is open".format(port))