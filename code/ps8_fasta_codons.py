#!/usr/bin/env python3
import sys
import re

#have a fasta file with >geneID followed by lines of sequence
#dictionaries have {}
fastaDict = {}

#open from user input and read the text line by line
with open(sys.argv[1],"r") as file_read:
    for line in file_read:
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
# print(fastaDict)
#access sequence
with open("Python_08.codons-frame-1.nt", "w") as file:
    for gene in fastaDict:
        sequence = fastaDict[gene]
        codons = re.findall(r"(.{3})", sequence)
        # print(codons)
        file.write(f'{gene}-frame-1-codons\n{codons[0]} {codons[1]} {codons[2]} {codons[3]}\n')