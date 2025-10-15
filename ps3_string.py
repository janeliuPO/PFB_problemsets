#!/usr/bin/env python3
import sys

dna_orig = sys.argv[1] #this allows me to paste in the sequence when running the command

dna_seq = dna_orig.upper() #this converts the sequence to uppercase

print(f"The number of A's, C's, G's, and T's in my sequence are {
dna_seq.count('A')}, {dna_seq.count('C')}, {dna_seq.count('G')}, and {dna_seq.count('T')}, respectively.")

# use f-string to format exactly what I want in terms of counting the A, C, G, and T nt

rna_seq = dna_seq.replace('T','U') #converts the DNA sequence in upper case to RNA

print(f"The RNA sequence of this DNA is: {rna_seq}.")

print(f'The total lenght of my sequence is: {len(dna_seq)}.') #counts total number of nt
gc_content = dna_seq.count('C')+dna_seq.count('G') #sums the G and C numbers
print(gc_content)

print(f'The GC content of the sequence is {gc_content/(len(dna_seq)):.2%}.') #divide by the total length and make into a percentage to get GC content