#!/usr/bin/env python3
import sys
import re
#eta - this was originally from PS5_fasta_dict_set.py - here, want to modify to use re
 
#open file
#read each line
#header line or sequence line
#format is >seqID\nsequence\nsequence
#want to create a dictionary with seqID as KEY and sequences as values

#dictionaries have {}
fastaDict_re = {}

#open and read the text line by line
with open("Python_06.fasta","r") as fasta_read:
    for line in fasta_read:
        line = line.rstrip()
        if re.search(r">", line):
            # print(line)
            for found in re.finditer(r">(\S+.*)", line):
                seqID = found.group(1)
                # print(seqID)
                fastaDict_re[seqID] = ''
        else: 
            fastaDict_re[seqID] += line

            
print(fastaDict_re)