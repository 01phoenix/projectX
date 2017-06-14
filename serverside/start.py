#!/usr/bin/python
import os,commands,time,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.10.134"
s_port=8888

s.bind(("",8888))

cdata=s.recvfrom(100)
#cdata1=s.recvfrom(100)

if cdata[0] == "test" :
	s.sendto("ok",cdata[1]) 
	
 
