#!/usr/bin/env python3
import sys
import re

def dna_num(dna, width):
    clean_dna = re.sub(r"\s+", "", dna) #replace all non-characters with nothing
    chunks = []
    for i in range(0, len(clean_dna), width):
        chunks.append(clean_dna[i:i+width])
    #if printing to Python can use \n
    #if writing to text file, then \n will be saved
    #for i in range(0, len(clean_dna), width) = iterating through the string
    #or list clean_dna in fixed-size steps, defined by the variable width. 
    #start = 0, starting index
    #stop = len(clean_dna) is ending index of the sequence
    #step = width
    return chunks

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
width = 80
print(dna_num(dna, width))
dna_length = [len(s) for s in dna_num(dna, width)]
print(dna_length)
# for sequence in dna_list(dna):
#     print(sequence)