#!/usr/bin/env python3
import sys
import re

def gc_content(dna):
    if not dna: #makes sure a string was entered
        return 0.0
    gc_count = dna.count('G') + dna.count('C')
    return round((gc_count / len(dna)) * 100)

dna = 'aagggAAGtt'
print(f'The GC content of the sequence is {gc_content(dna)}%.')