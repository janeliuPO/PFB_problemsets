#!/usr/bin/env python3
import sys

#want to open and read contents of a file
#then uppercase each line and rstrip at the same time!
#then write each line to next text file

with open("Python_06.txt","r") as text_read, open("Python_06_uc.txt","w") as text_write:
    for line in text_read:
        line = line.rstrip().upper()
        text_write.write(f'{line}\n')
                         
print("Finished writing 'Python_06_uc.txt'")