#!/usr/bin/env python3
import sys
import re

#oepn and read the whole text
shel = open("Python_07_nobody.txt", "r")
contents = shel.read()

#use re.sub to substitute Greg for Nobody
new_contents = re.sub(r"Nobody", r"Greg", contents)
print(contents)
print(new_contents)        
with open("Python_07_Greg.txt", "w") as file_object:
    file_object.write(new_contents)                                          