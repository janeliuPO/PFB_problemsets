#!/usr/bin/env python3
import sys
import re

class DNASequence(object):

    def __init__(self, sequence, seq_name, organism):
        self.sequence = sequence.upper()
        self.seq_name = seq_name
        self.organism = organism
    
def dna_rc(self):
    clean_dna = re.sub(r"\s+", "", self) 
    #replace all non-characters with nothing
    seq = clean_dna.upper()
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')
    seq = seq[::-1]
    return seq.upper()

dna_seq1 = DNASequence('agagagtttccc', 'test1', 'bunnies')
dna_seq2 = DNASequence('aaggttaaggtt', 'test2', 'panda')

for input in [dna_seq1,dna_seq2]:
    print(f'{input.seq_name} has the sequence: {input.sequence} and is from {input.organism}.')
