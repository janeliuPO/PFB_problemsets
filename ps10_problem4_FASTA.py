#!/usr/bin/env python3
import sys
import re

def dna_num(file_read):
    fastaDict = {}
    #open from user input and read the text line by line
    with open(sys.argv[1],"r") as file_read:
        for line in file_read:
            line = line.rstrip()
            if line.find('>') == 0:
                seqID = line
                #does key already exist in the dictionary
            else:
                if seqID in fastaDict:
                    seq = fastaDict[seqID] + line
                    fastaDict[seqID] = seq
                else: 
                    fastaDict[seqID] = line
                chunks = []
                for key in fastaDict:
                    value = fastaDict[key]
                    for i in range(0, len(value), width):
                        chunks.append(value[i:i+width])
                    fasta = f'{seqID}\n{chunks}\n'

    # chunks = []
    # for i in range(0, len(clean_dna), width):
    #     chunks.append(clean_dna[i:i+width])
    #if printing to Python can use \n
    #if writing to text file, then \n will be saved
    #for i in range(0, len(clean_dna), width) = iterating through the string
    #or list clean_dna in fixed-size steps, defined by the variable width. 
    #start = 0, starting index
    #stop = len(clean_dna) is ending index of the sequence
    #step = width
    return fasta

file_read = sys.argv[1]
width = 5
print(dna_num(file_read))
# dna_length = [len(s) for s in dna_num(dna, width)]
# print(dna_length)
# for sequence in dna_list(dna):
#     print(sequence)