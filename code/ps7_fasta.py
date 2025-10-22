#!/usr/bin/env python3
import sys
import re

#oepn and read the whole text
fasta_file = open("Python_07.fasta.txt", "r")
contents = fasta_file.read()

#findall the headers with seqName and description use pattern matching
#starts with >... then any series of non-spaces, followed by space, and then any character, including spaces
#group(1) is the seqName and group(2) is the descriptor
#great for loop - see backside of page 7-5
for found in re.finditer(r">(\S+) (.+)", contents):
    print(f'id:{found.group(1)} descr:{found.group(2)}')


