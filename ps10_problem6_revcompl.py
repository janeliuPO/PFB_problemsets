#!/usr/bin/env python3
import sys
import re

def dna_rc(dna):
    clean_dna = re.sub(r"\s+", "", dna) 
    #replace all non-characters with nothing
    seq = clean_dna.upper()
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')
    seq = seq[::-1]
    return seq.upper()

dna = 'GGA aat CC\n'
print(f'The reverse complement of {dna} is {dna_rc(dna)}.')