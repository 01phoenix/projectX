#!/usr/bin/python2

import socket
import os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",9999))


while  True :
    data=s.recvfrom(100)
    os.system('openssl base64 -d -des3 -in send.py')
    print  "message  from  client  :   ",data[0]
    print  "__________________________________"
    print   "Client  address  :  ",data[1][0]
    print  "__________________________________"
    os.system('openssl base64 -e -des3 -in recv.py')
    r=raw_input("type your reply :  ")
    s.sendto(r,data[1])
