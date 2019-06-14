#!/usr/bin/python3

#Python Program which performs similar operation like "Touch" shell command

import os
import datetime
import time

choice = int(input("Enter you Choice : \n 1. touch \t2.touch -d\t3.touch -c\t4.touch multiple files\t5.touch -r\n:"))

#OPEN the FILE
#Normal create an empty file using touch function
if choice==1:
    loc=input("Enter file name with path to create it\n")
    myfile=open(loc,"w")
    myfile.close()


#With -d update the access and modification times
elif choice==2:
    loc=input("Enter file name with path to change its modification and time to current time\n")
    os.utime(loc)

#With -c file does not exist, do not create
elif choice==3:
     
    loc=input("Enter file name with path to check whether exist or not\n")
    try:
        open(loc,"r")
        print("File exist")
    except:
        print("File not crated")
    

# create multiplefile :
elif choice==4:
    locs=[]
    num=int(input("Enter Number of new files to create"))
    for i in range(num):
        loc=input("Enter name of file "+str(i)+" with location\n")
        myfile=open(loc,"w")
        myfile.close()

# with -r access and modification times of file
elif choice==5:
    lop=input("Enter File path from which upadated date and time is extracted\n")
    loc=input("Enter File path To Update date and time\n")

os.utime(loc,(os.path.getmtime(lop),os.path.getmtime(lop)))

