#!/usr/bin/python2

import  socket
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip="192.168.43.21"
server_port=9999


while True :
    os.system('openssl base64 -e -des3 -in send.py')
    msg=raw_input("enter your message :   ")
    s.sendto(msg,(server_ip,server_port))	
    os.system('openssl  base64 -d -des3 -in recv.py')
    print  s.recvfrom(100)


