#!/usr/bin/env python3
import sys
import re
reDict_bionet = {}

#open and read the text line by line
file = open("bionet.txt","r")
content = file.readlines() #this allows me to limit the lines we read
    
for line in content[11:-1]:
    # print(line)
    line = line.rstrip()
    list = re.split(r" {4,}", line)
    print(list)
    reName = list[0]
    # print(reName)
    site = list[1]
    reDict_bionet[reName] = site

print(reDict_bionet)
