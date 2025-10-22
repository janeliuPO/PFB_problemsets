#!/usr/bin/env python3
import sys

#want to open and read contents of a file
#then uppercase each line
#then print each line to standard output

with open("Python_06.txt","r") as text_obj:
    for line in text_obj:
        line = line.rstrip().upper()
        print(line)