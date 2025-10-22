#!/usr/bin/env python3
import sys


#open file
#read each line
#header line or sequence line
#format is >seqID\nsequence\nsequence
#want to create a dictionary with seqID as KEY and sequences as values

#dictionaries have {}
fastaDict = {}

with open("Python_06.fasta","r") as fasta_read:
    for line in fasta_read:
        line = line.rstrip()
        if line.find('>') == 0:
            seqID = line.lstrip('>')
            #does key already exist in the dictionary
        else:
            seq = line
            if seqID in fastaDict:
                value = fastaDict[seqID] + line
                fastaDict[seqID] = value
            else: 
                fastaDict[seqID] = line
            
print(fastaDict)