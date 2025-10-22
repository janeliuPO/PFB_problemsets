#!/usr/bin/env python3
import sys
import re
from Bio import SeqIO

filename = sys.argv[1]
fasta_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
total_seqs = len(fasta_dict)
print(f'total sequences: {total_seqs}')
# print(fasta_dict)

substring = 'Salmonella paratyphi B'
matching_items = {}

for seq_record in SeqIO.parse(filename, "fasta"):
    description = seq_record.description
    sequence = seq_record.seq
    gene_id = seq_record.id
    # print(description)
    # print(sequence)
    # print(gene_id)
    for found in re.findall(r"Salmonella paratyphi B", description):
        matching_items[gene_id] = sequence

print(matching_items)

with open("s_paratyphi.prot.fa", "w") as file:
    for key, value in matching_items.items():
        file.write(f'>{key}\n{value}\n')

