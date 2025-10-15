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

at_content = dna_seq.count('A')+dna_seq.count('T') #sums the A and T numbers
print(at_content)

print(f'The AT content of the sequence is {at_content/(len(dna_seq)):.2%}.') #divide by the total length and make into a percentage to get AT content

reverse_dna_seq = dna_orig[::-1] #reverse the dna_seq
print(reverse_dna_seq)
wxyz_complement = reverse_dna_seq.replace('A','W').replace('C','X').replace('G','Y').replace('T','Z').replace('a','w').replace('c','x').replace('g','y').replace('t','z') #convert the A's to X's, a's to x's etc - the change to x or x prevents the things I just changed to be change again.
rev_complement = wxyz_complement.replace('W','T').replace('X','G').replace('Y','C').replace('Z','A').replace('w', 't').replace('x','g').replace('y', 'c').replace('z', 'a') #convert the W's and w's to T's, t's - this should be the rev complement!
print(f'The reverse complement of my DNA sequence is: {rev_complement}.')

sub_dna = dna_seq[0:] #extracts and prints nt from 100-200
print(sub_dna)

sub_gc_content = sub_dna.count('C')+sub_dna.count('G') #sums the G and C numbers

print(f'The GC content of the sub-sequence is {sub_gc_content/(len(sub_dna)):.2%}.') #divide by the total length and make into a percentage to get GC content


