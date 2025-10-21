#!/usr/bin/env python3
import sys
from Bio import SeqIO

filename = sys.argv[1]
fasta_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
total_seqs = len(fasta_dict)
# print(fasta_dict)
print(f'total nuber of sequences: {total_seqs}')

nt_count = 0
gc_count = 0
seq_list = []
gc_dict = {}
for seq_record in SeqIO.parse(filename, "fasta"):
    gene_id = seq_record.id
    sequence = seq_record.seq
    seq_upp = sequence.upper()
    nt_count += len(sequence)
    seq_list.append(str(seq_record.seq)) #add only sequences to list
    count_C = str(seq_upp).count('C')
    # print(len(sequence))
    # print(count_C)
    count_G = str(seq_upp).count('G')
    # print(count_G)
    gc = ((count_G + count_C)/len(sequence))
    gc_dict[gene_id] = gc
    gc_count += ((count_G + count_C)/len(sequence))
    # print(gc)
    # print(sequence)
    # print(f'{gene_id}: {sequence}')
    # print(f'gc content: {gc_content:.2%}')
# print(seq_list)
# print(gc_dict)
sorted_list = sorted(seq_list, key=len, reverse=False)
gc_pct = gc_count/total_seqs

# print(sorted_list)
print(f'total number of nucleotides: {nt_count}')
print(f'average length of sequences: {nt_count/total_seqs}')
print(f'shortest sequence length: {len(sorted_list[0])}')
print(f'longest sequence length: {len(sorted_list[-1])}')
print(f'average gc content of sequences: {gc_pct:.2%}')
sorted_gc = sorted(gc_dict.items(), key=lambda item: item[1])
smallest_key, smallest_value = sorted_gc[0]
largest_key, largest_value = sorted_gc[-1]
print(f'lowest GC content: {smallest_key}: {smallest_value:.2%}')

print(f'highest GC content: {largest_key}: {largest_value:.2%}')

