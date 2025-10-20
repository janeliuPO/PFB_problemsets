#!/usr/bin/env python3
import sys
import re

def dna_gc(dna):
    clean_dna = re.sub(r"\s+", "", dna) 
    #replace all non-characters with nothing
    g_count = clean_dna.count('G')
    c_count = clean_dna.count('C')
    total_nt = len(clean_dna)
    gc_content = (g_count + c_count)/(total_nt)
    return gc_content

dna = 'GGA ATT CC\n'
print(f'The GC content of the sequence is {dna_gc(dna):.2%}.')