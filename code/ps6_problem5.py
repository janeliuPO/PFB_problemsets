#!/usr/bin/env python3
import sys

tf_all = set()
stemcell_prolif = set()
with open("ferret_all_genes.tsv","r") as all_genes:
    for line in all_genes:
        tf_all.add(line.strip())

with open("ferret_stemcellproliferation_genes.tsv","r") as stemcell_genes:
    for line in stemcell_genes:
        stemcell_prolif.add(line.strip())
bothgenes = tf_all & stemcell_prolif
print(bothgenes)
