#!/usr/bin/env python3
import sys

dna_orig = sys.argv[1] #this allows me to paste in the sequence when running the command

dna_seq = dna_orig.upper() #this converts the sequence to uppercase

print(dna_seq.find('GAATTC') + 1)
