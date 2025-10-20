#!/usr/bin/env python3
import sys
import re

def dna_num(file_read):
    fastaDict = {}
    width = int(sys.argv[2])
    #open from user input and read the text line by line
    with open(sys.argv[1],"r") as file_read:
        for line in file_read:
            line = line.rstrip()
            if line.find('>') == 0:
                seqID = line
            else:
                chunks = []
                for i in range(0, len(line), width):
                    chunks.append(line[i:i+width])
                if seqID not in fastaDict:
                    fastaDict[seqID] = chunks
                else: 
                    fastaDict[seqID].append(chunks)
    fasta_file = "" #anytime want a string, list, etc to be added to,
    #have outside of loop
    for seqID, chunks in fastaDict.items():    
        fasta_file += f'{seqID}\n{"\n".join(chunks)}\n' 
    return fasta_file

file_read = sys.argv[1]
width = sys.argv[2]
fo = open("Python_10.output.fa", "w")
fo.write(dna_num(file_read))