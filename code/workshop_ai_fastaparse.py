#!/usr/bin/env python3
import sys
import re

def parse_fasta(filename):
    sequences = {}
    with open(filename, 'r') as file:
        seq_name = ''
        seq_data = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if seq_name:
                    sequences[seq_name] = ''.join(seq_data)
                seq_name = line[1:]  # Remove '>'
                seq_data = []
            else:
                seq_data.append(line.upper())
        if seq_name:
            sequences[seq_name] = ''.join(seq_data)
    return sequences

def nucleotide_composition(sequences):
    for name, seq in sequences.items():
        counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0} #defining a dictionary
        for nucleotide in seq: #for each item in the value, here, character in string
            if nucleotide in counts:
                counts[nucleotide] += 1
        print(f"{name}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")
    
filename = sys.argv[1]
sequences = parse_fasta(filename) 
print(parse_fasta(filename))
print(nucleotide_composition(sequences))
