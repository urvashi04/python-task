#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


msg=raw_input("enter your message:  ")
s.sendto(msg,(recv_ip,recv_port))
print(s.recvfrom(50))
print(msg)
 
if len(msg)>150:
 print("message length is exceded")

else:
 print("exit the conversation")

choice = raw_input("enter your choice : 1. continue message , else press enter to exit")

if choice =="1":
 while 4>3:
    msg=raw_input("enter your message: ")
    s.sendto(msg,(recv_ip,recv_port))
    print(s.recvfrom(50))
    print(msg)

else:
    print("conversation is aborted")



s.close()




