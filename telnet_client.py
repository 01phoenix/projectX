#!/usr/bin/python2

import  socket,os,commands,time,sys

sip="192.168.43.21"
sport=1234

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# telnet  server  username  
user=raw_input("enter  user name :  ")
#password=raw_input("enter  user password  :  ")
#cmd=commands.getoutput('useradd '+u)
os.system('useradd '+user)
#enter password for the user created above
print "enter password for "+user
os.system('passwd '+user)

s.sendto(user,(sip,sport))
#s.sendto(password,(sip,sport))

print  s.recvfrom(100)
while  True :
	cmd=raw_input("[root@station171 ]# ")
	s.sendto(cmd,(sip,sport))
	print   s.recvfrom(100)[0]


