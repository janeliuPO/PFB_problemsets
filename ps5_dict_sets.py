#!/usr/bin/env python3
import sys

#input DNA seq from command line
dna = sys.argv[1]

#determine unique characters
unique = set(dna)
print(f'The DNA sequence includes the following unique nucleotides: {unique}.')

nt_count = {}
for nt in unique:
    count = dna.count(nt)
    nt_count[nt] = count
print(f'The nt distribution is: {nt_count}')
