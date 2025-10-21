#!/usr/bin/env python3
import sys
from Bio import SeqIO

filename = sys.argv[1]
fasta_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
total_seqs = len(fasta_dict)
# print(fasta_dict)
print(f'total nuber of sequences: {total_seqs}')


for seq_record in SeqIO.parse(filename, "fasta"):
    gene_id = seq_record.id
    sequence = seq_record.seq
    # aa_count += len(sequence)
    # print(sequence)


with open("ps_blast.out", "w") as fasta_file:
    fasta_file.write(fasta_dict[0])
# # print(sorted_list)
# print(f'total number of nucleotides: {nt_count}')
# print(f'average length of sequences: {nt_count/total_seqs}')
# print(f'shortest sequence length: {len(sorted_list[0])}')
# print(f'longest sequence length: {len(sorted_list[-1])}')
# print(f'average gc content of sequences: {gc_pct:.2%}')
# sorted_gc = sorted(gc_dict.items(), key=lambda item: item[1])
# smallest_key, smallest_value = sorted_gc[0]
# largest_key, largest_value = sorted_gc[-1]
# print(f'lowest GC content: {smallest_key}: {smallest_value:.2%}')

# print(f'highest GC content: {largest_key}: {largest_value:.2%}')

