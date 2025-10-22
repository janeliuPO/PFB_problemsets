#!/usr/bin/env python3
import sys
import re

def dna_60(dna):
    clean_dna = re.sub(r"\s+", "", dna) #replace all non-characters with nothing
    sub_dna = re.sub(r"(.{60})", r"\1^", clean_dna)
    #if printing to Python can use \n
    #if writing to text file, then \n will be saved
    dna_list = sub_dna.split('^')
    # dna_length = [len(s) for s in dna_list]
    # for line in dna_list:
    #     line_length = len(line)
    return dna_list

dna = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

print(dna_60(dna))
dna_length = [len(s) for s in dna_60(dna)]
print(dna_length)
# for sequence in dna_list(dna):
#     print(sequence)