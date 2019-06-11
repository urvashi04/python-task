#!/usr/bin/python3

import datetime
name = input("what your name:")
print(name)
currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
 print('good morning')
elif 12 <= currentTime.hour < 16:
 print('good afternoon')
elif 16 <= currenttime.hour < 18:
 print('good evening')
else:
 print('good night')

