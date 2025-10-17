#!/usr/bin/env python3
import sys


#open file
#read each line
#header line or sequence line
#format is >seqID\nsequence\nsequence
#want to create a dictionary with seqID as KEY and sequences as values

#dictionaries have {}
fastaDict = {}

with open("fastapractice.txt","r") as fasta_read:
    for line in fasta_read:
        line = line.rstrip()
        if line.find('>') == 0:
            seqID = line.lstrip('>')
        else:
            fullseq = line
            fastaDict[seqID] = fullseq

print(fastaDict)