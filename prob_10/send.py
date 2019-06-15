#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
n=raw_input("enter your choice:  1) from both side msg 2) from one side msg")

if n == "1":
 msg=raw_input("enter your message:  ")
 s.sendto(msg,(recv_ip,recv_port))
 print(s.recvfrom(50))
 print(msg)

elif n == "2":
 msg=raw_input("enter your message:  ")
 s.sendto(msg,(recv_ip,recv_port))

else:
    print("enter valid choice: ")




