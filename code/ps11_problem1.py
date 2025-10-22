#!/usr/bin/env python3
import sys
import re

class DNASequence(object):
    def __init__(self, sequence, seq_name, organism):
        self.sequence = sequence.upper()
        self.seq_name = seq_name
        self.organism = organism
    
def dna_length(dna):
    clean_dna = re.sub(r"\s+", "", dna) 
    total_nt = len(clean_dna)
    return total_nt

def dna_counts(dna):
    clean_dna = re.sub(r"\s+", "", dna) 
    #replace all non-characters with nothing
    seq = clean_dna.upper()
    count_A = seq.count('A')
    count_T = seq.count('T')
    count_C = seq.count('C')
    count_G = seq.count('G')
    counts = f'the number of As is: {count_A}, the number of Ts is: {count_T}, the number of Cs is: {count_C}, and the number of Gs is: {count_G}.'
    return counts

def dna_gc(dna):
    clean_dna = re.sub(r"\s+", "", dna) 
    #replace all non-characters with nothing
    seq = clean_dna.upper()
    count_C = seq.count('C')
    count_G = seq.count('G')
    total_nt = len(clean_dna)
    gc_content = (count_G + count_C)/(total_nt)
    return gc_content

dna_seq1 = DNASequence('agagagtttccc', 'test1', 'bunnies')
dna_seq2 = DNASequence('aaggttaaggtt', 'test2', 'panda')

with open("Python_11.output.fa", "w") as file:
    for input in [dna_seq1,dna_seq2]:
    # print(f'{input.seq_name}({input.organism}) has the sequence: {input.sequence} with a length of {dna_length(input.sequence)}.')
    # print(f'For {input.seq_name}, {dna_counts(input.sequence)}')
    # print(f'The GC content is {dna_gc(input.sequence):.2%}')
        file.write(f'>{input.seq_name}\n{input.sequence}\n')