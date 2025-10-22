#!/usr/bin/env python3
import sys
import re

#have a fasta file with >geneID followed by lines of sequence
#dictionaries have {}
fastaDict = {}

#open and read the text line by line
with open("Python_08.fasta.txt","r") as fasta_read:
    for line in fasta_read:
        line = line.rstrip()
        if line.find('>') == 0:
            remove = line.lstrip('>')
            # print(remove)
            id_list = remove.split()
            # print(id_list)
            gene_name = id_list[0]
            # print(gene_name) 
            #does key already exist in the dictionary
        else:
            seq = line
            if gene_name in fastaDict:
                value = fastaDict[gene_name] + line
                fastaDict[gene_name] = value
            else: 
                fastaDict[gene_name] = line

#access sequence
for gene in fastaDict:
    sequence = fastaDict[gene]
    A_count = sequence.count('A')
    T_count = sequence.count('T')
    C_count = sequence.count('C')
    G_count = sequence.count('G')
    print(f'{gene}\t{A_count}\t{T_count}\t{G_count}\t{C_count}')
