#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recv_ip,recv_port))

n=raw_input("enter your choice:  1)from both side msg  2)from one side msg")

if n == "1":
 data=s.recvfrom(150)
 print("message from sender",data)
 msg=raw_input("enter your reply:  ")
 s.sendto(msg,data[0])

elif n == "2":
 data=s.recvfrom(150)
 print("message from sender",data)
 

else:
    print("enter valid choice: ")
    



