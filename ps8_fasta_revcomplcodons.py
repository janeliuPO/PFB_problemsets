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
#access reverse sequence
rev_codons_list = []
with open("Python_08.codons-6frames.nt", "w") as file:
    for gene in fastaDict:
        sequence = fastaDict[gene]
        reverse_seq = sequence[::-1] #reverse each line
        wxyz_complement = reverse_seq.replace('A','W').replace('C','X').replace('G','Y').replace('T','Z').replace('a','w').replace('c','x').replace('g','y').replace('t','z') #convert the A's to X's, a's to x's etc - the change to x or x prevents the things I just changed to be change again.
        rev_complement = wxyz_complement.replace('W','T').replace('X','G').replace('Y','C').replace('Z','A').replace('w', 't').replace('x','g').replace('y', 'c').replace('z', 'a') #convert the W's and w's to T's, t's - this should be the rev complement!
        # print(sequence)
        # print(rev_complement)
        for start in range(3):
            rev_codons_list += [re.findall(r"(.{3})", rev_complement[start:])]
        # print(codons_list[1])
        file.write(f'{gene}-frame-1-codons\n{rev_codons_list[0][0]} {rev_codons_list[0][1]}\n{gene}-frame-2-codons\n{rev_codons_list[1][0]} {rev_codons_list[1][1]}\n{gene}-frame-3-codons\n{rev_codons_list[2][0]} {rev_codons_list[2][1]}\n')
    #getting codons in all three frames

