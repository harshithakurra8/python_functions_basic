#  Write a Python program to valid a IP address

import socket
addr='127.23.4.4545'
try:
    socket.inet_aton(addr)
    print("Valid Ip")
except socket.error:
    print("Invalid IP")