#!/usr/bin/env python3
import sys
import re

#two dictionaries - one I make from fasta file, one provided
#Dict from a Fasta file with a >gene_ID followed by description
fastaDict = {}
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}
#open and read file line by line, and write to two different files
with open(sys.argv[1],"r") as file_read, open("Python_08.codons-6frames.nt", "w") as file_nt, open("Python_08.translated.aa", "w") as file_aa:
    for line in file_read:
        line = line.rstrip()
        if line.find('>') == 0: #looking for >geneID
            remove = line.lstrip('>') #this will now be ONLY geneID
            # print(remove)
            id_list = remove.split() #this will create a list now for each geneID line
            # print(id_list)
            gene_name = id_list[0] #this will only be the first item of the list, which is the geneID - not the description
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

    for gene in fastaDict: #going through Dict, key by key
        translation_frames = [] #will be a list of lists
        rev_translation_frames = [] #will be a list of lists
        sequence = fastaDict[gene] #getting value from key
        for start in range(3):
            translation_frames += [re.findall(r"(.{3})", sequence[start:])]
        print(f'The three frames are: {translation_frames}') #this level of indentation gives me one list per gene

        reverse_seq = sequence[::-1] #reverse each sequence
        wxyz_complement = reverse_seq.replace('A','W').replace('C','X').replace('G','Y').replace('T','Z').replace('a','w').replace('c','x').replace('g','y').replace('t','z') #convert the A's to X's, a's to x's etc - the change to x or x prevents the things I just changed to be change again.
        rev_complement = wxyz_complement.replace('W','T').replace('X','G').replace('Y','C').replace('Z','A').replace('w', 't').replace('x','g').replace('y', 'c').replace('z', 'a') #convert the W's and w's to T's, t's - this should be the rev complement!
        # print(sequence)
        # print(rev_complement)
        for start in range(3):
            rev_translation_frames += [re.findall(r"(.{3})", rev_complement[start:])]
        print(f'The three frames on the reverse strand are: {rev_translation_frames}')

        #format the output table
        i=1 #looping
        for frame in translation_frames:#identifying the list in my list of lists
            print(f'{gene}-frame-{i}-codons and aa:')
            nt_seq=''
            protein=''
            for codon in frame:#identifying the object in my list
                nt_seq += codon + ' '
                protein += f'{translation_table[codon]} '
        #         # print(codon) <-- alternative way
        #         # print(" ") <-- alternative way
            print(nt_seq)
            print(protein)
            file_nt.write(f'{gene}-frame-{i}-codons\n{nt_seq}\n')
            file_aa.write(f'{gene}-frame-{i}-codons\n{protein}\n')
            i+=1

        i=1
        for frame in rev_translation_frames:
            print(f'{gene}-rev-frame-{i}-codons and aa:')
            nt_seq_rev=''#not really necessary here because of join.frame
            protein_rev=''
            for codon in frame:#identifying the object in my list
                nt_seq_rev += codon + ' '
                protein_rev += f'{translation_table[codon]} '
            print(" ".join(frame))
            print(protein_rev)
            file_nt.write(f'{gene}--rev-frame-{i}-codons\n{nt_seq_rev}\n')
            file_aa.write(f'{gene}-rev-frame-{i}-codons\n{protein_rev}\n')
            i+=1


