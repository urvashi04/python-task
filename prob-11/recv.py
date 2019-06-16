#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))

data=s.recvfrom(150)
print("message from sender",data[0])
print("sender IP + port --socket:",data[1])
msg=raw_input("enter your reply :")

if len(msg)>150:
 print("message length is exceeded")
 

else:
 s.sendto(msg,data[1])

choice = raw_input("enter your choice : 1. continue message , else press enter to exit ")

if choice =="1":
 while 4>3:
    data=s.recvfrom(150)
    print("message from sender: ",data[0])
    print("sender IP+PORT --socket: ",data[1])
    msg=raw_input("enter your reply: ")
    s.sendto(msg,data[1])

else:
    print("conversation is aborted")

s.close()


    



