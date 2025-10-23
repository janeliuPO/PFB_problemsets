#!/usr/bin/env python

import os, sys, math, re

#method to generate a table containing the number of reads mapped to each gene
#open sam file, which is tab deliminated
#[0] is a read name - should only have read names once
#[1] is ??
#[2] gene name

file_name = sys.argv[1]
gene_reads = {}


with open(file_name, "r") as read:
    for line in read:
        line = line.rstrip()
        columns = re.split(r"\t", line)
        # print(list)
        readname = columns[0]
        print(readname)
        gene_ID = columns[2]
        # print(gene_ID)
        gene_name = re.findall(r"(^.+)\^", gene_ID)
        # print(gene_name)
        if readname not in gene_reads:
            gene_reads[readname] = gene_name
        else:

        # else:
        #     gene_reads_dict[gene_name].append(readname)

# print(gene_reads_dict)