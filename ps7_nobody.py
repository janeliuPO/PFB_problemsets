#!/usr/bin/env python3
import sys
import re

#oepn and read the whole text
shel = open("Python_07_nobody.txt", "r")
contents = shel.read()

#use finditer to find position of the subpattern matches
for found in re.finditer(r"Nobody", contents):
    print("position:" , found.start(), found.end(), sep="\t")