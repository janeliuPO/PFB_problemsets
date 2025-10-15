#!/usr/bin/env python3
import sys

dna_orig = sys.argv[1] #this allows me to paste in the sequence when running the command

dna_seq = dna_orig.upper() #this converts the sequence to uppercase

print(f"The number of A's, C's, G's, and T's in my sequence are {
dna_seq.count('A')}, {dna_seq.count('C')}, {dna_seq.count('G')}, and {dna_seq.count('T')}, respectively.")
