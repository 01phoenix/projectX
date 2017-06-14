#!/usr/bin/python
import os,commands,socket,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.43.200"
s_port=8888

os.system("ssh -X test@"+s_ip+ " firefox")
execfile("saas.py")

