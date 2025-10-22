#!/usr/bin/env python3
import sys
import re

class NotFASTAError(Exception):
    pass
file = ''
try: 
    file = sys.argv[1]
    print(f'User provided file: {file}. Thank you!')
    if not file.endswith('.fasta', '.fa', '.nt'):
        raise NotFASTAError("Not a FASTA file")
except:
    print('Please provide a fasta file.')
except NotFASTAError:
    print("File needs to be a FASTA file")
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
with open("Python_08.codons3frames.nt", "w") as file:
    codons_list = []
    for gene in fastaDict:
        sequence = fastaDict[gene]
        # print(sequence)
        for start in range(3):
            codons_list += [re.findall(r"(.{3})", sequence[start:])]
        # print(codons_list[1])
        file.write(f'{gene}-frame-1-codons\n{codons_list[0][0]} {codons_list[0][1]}\n{gene}-frame-2-codons\n{codons_list[1][0]} {codons_list[1][1]}\n{gene}-frame-3-codons\n{codons_list[2][0]} {codons_list[2][1]}\n')