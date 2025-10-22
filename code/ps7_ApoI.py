#!/usr/bin/env python3
import sys
import re
fastaDict_re = {}

#open and read the text line by line
with open("Python_07_ApoI.fasta","r") as fasta_read:
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

# print(fastaDict_re)

new_fasta = re.sub(r"([AG])(AATT[CT])", r"\1^\2", fastaDict_re['seq1'])
# print(new_fasta)

cuts = new_fasta.split('^')
print(cuts)