#!/usr/bin/python
import os,socket,commands,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.43.200"
s_port=8888

x="""
press 1 for firefox 
press 2 for vlc
press 3 for gedit
"""
print x
ch=raw_input()

if ch == '1' : 
	print "Wait for few seconds..."
	#os.system("ssh -X test@"+s_ip+"firefox")
	execfile("firefox.py")
else : 
	exit() 
