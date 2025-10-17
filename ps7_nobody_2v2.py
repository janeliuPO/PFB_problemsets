#!/usr/bin/env python3
import sys
import re

#oepn and read the whole text
shel = open("Python_07_nobody.txt", "r")
contents = shel.read()

#use re.sub to substitute Greg for Nobody and immediatedly write to new file
with open("Python_07_Gregv2.txt", "w") as file_object:
    file_object.write(re.sub(r"Nobody", r"Greg", contents))                                          