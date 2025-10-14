#!/usr/bin/env python3
import sys

count = int(sys.argv[1]) #allows me to add number to command line and convet that to an intenger that can be compared

if count > 0 and count < 50: #positive number
    if count%2 == 0:
        print("it is an even number that is smaler than 50")
    else:
        print("positive, odd")

elif count > 0 and count > 50: #positive number
    if count%3 == 0:
        print("it is a number divisible by 3 that is greater than 50")
    else:
        print("positive, >50")

elif count < 0: #negative number
    print("negative")

elif count == 50:
    print("50")
    
else: #zero
    print("number is zero")
