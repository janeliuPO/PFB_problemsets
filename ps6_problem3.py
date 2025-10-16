#!/usr/bin/env python3
import sys

#want to open and read contents of a file with sequences
#format of file is seqName\tsequence\n.
#then do reverse complement of each line
#then print each line

with open("Python_06.seq.txt","r") as text_read:
    for line in text_read:
        line = line.split()
        sequence = line[1]
        reverse_seq = sequence[::-1] #reverse each line
        wxyz_complement = reverse_seq.replace('A','W').replace('C','X').replace('G','Y').replace('T','Z').replace('a','w').replace('c','x').replace('g','y').replace('t','z') #convert the A's to X's, a's to x's etc - the change to x or x prevents the things I just changed to be change again.
        rev_complement = wxyz_complement.replace('W','T').replace('X','G').replace('Y','C').replace('Z','A').replace('w', 't').replace('x','g').replace('y', 'c').replace('z', 'a') #convert the W's and w's to T's, t's - this should be the rev complement!
        print(f'>{line[0]}\n{rev_complement}')