#!/usr/bin/python

import os,commands,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.43.200"
s_port=8888
print "services are loading!"
time.sleep(2)

s_user=raw_input("Enter username : ")
s_password=raw_input("Enter passwd : ")

s.sendto(s_user,(s_ip,s_port))
s.sendto(s_password,(s_ip,s_port))

sdata=s.recvfrom(2)

if sdata[0] == "ok" : 
	print "authentication done"
	print "wait for services "
	time.sleep(2)
	execfile("saas.py")
else : 
	print "wrong username and password"	
	exit()



