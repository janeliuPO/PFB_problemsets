#!/usr/bin/env python3
import sys
import re

#this doesn't work below because it needs to do things line by line
with open("Python_07_nobody.txt", "r") as contents, open("Python_07_Gregv3.txt", "w") as file_object:
    file_object.write(re.sub(r"Nobody", r"Greg", contents))                                          