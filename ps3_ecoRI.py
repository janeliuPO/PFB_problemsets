#!/usr/bin/env python3
import sys

dna_orig = sys.argv[1] #this allows me to paste in the sequence when running the command

dna_seq = dna_orig.upper() #this converts the sequence to uppercase

ecoRI_start = dna_seq.find('GAATTC') + 1 #this gives me the first nt position of the first ecoRI site

ecoRI_end = ecoRI_start + 6 #this gives me the last nt position of the first ecoRI site

print(f"""For the forward strand
      EcoRI startPos:{ecoRI_start} endPos:{ecoRI_end}""")

#below here, now do the reverse complement of the dna_seq

reverse_dna_seq = dna_seq[::-1] #reverse the dna_seq

wxyz_complement = reverse_dna_seq.replace('A','W').replace('C','X').replace('G','Y').replace('T','Z').replace('a','w').replace('c','x').replace('g','y').replace('t','z') #convert the A's to X's, a's to x's etc - the change to x or x prevents the things I just changed to be change again.
rev_complement = wxyz_complement.replace('W','T').replace('X','G').replace('Y','C').replace('Z','A').replace('w', 't').replace('x','g').replace('y', 'c').replace('z', 'a') #convert the W's and w's to T's, t's - this should be the rev complement!

ecoRI_start = rev_complement.find('GAATTC') + 1 #this gives me the first nt position of the first ecoRI site

ecoRI_end = ecoRI_start + 6 #this gives me the last nt position of the first ecoRI site

print(f"""For the opposite strand
      EcoRI startPos:{ecoRI_start} endPos:{ecoRI_end}""")
