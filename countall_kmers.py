#!/usr/bin/env python

import os, sys, math

from sequences_for_kmers import *
from extracting_kmers import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }

def count_kmers(kmer_list):

    kmer_count_dict = dict()

    ##################
    ## Step 2:
    ## begin your code

#take all_kmers list
#read list one item at a time, if not a key, then add as a key
#value = count

    for key in kmer_list:
        if key not in kmer_count_dict:
            kmer_count_dict[key] = 1
        else: 
            kmer_count_dict[key] += 1

    ## end your code
    ################

    return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = list()

    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences

# seq_list (output from sequences_for_kmers)
    #look through kmers  = sequence_to_kmer_list(sequence, kmer_length) which returns a kmer_list for a given sequence
    #for each object in seq_list from sequences*.py
    #put into extracting function, with kmer_length specified
    #that should produce kmer_list

    for sequence in seq_list:
        all_kmers.extend(sequence_to_kmer_list(sequence, kmer_length))

    # print(all_kmers)
    # print(count_kmers(all_kmers)) 
    ## end your code
    #######################

    kmer_count_dict = count_kmers(
        all_kmers
    )  # see step 2 above. You implement this. :-)

    unique_kmers = list(kmer_count_dict.keys())

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation

    sorted_dict = dict(sorted(kmer_count_dict.items() ,key=lambda kmers_tuple: kmers_tuple[1], reverse=True))
    sorted_keys = list(sorted_dict.keys())
    # print(sorted_kmers)

    # print(sorted_dict)
    ## end your code
    # sorted_dict[kmer] = [abund, entropy]
        
    for kmer, value in sorted_dict.items():
        sorted_dict[kmer] = [value]
        frac_A = float((kmer.count('A'))/(len(kmer)))
        frac_C = float((kmer.count('C'))/(len(kmer)))
        frac_G = float((kmer.count('G'))/(len(kmer)))
        frac_T = float((kmer.count('T'))/(len(kmer)))
        frac_list = [frac_A, frac_C, frac_G, frac_T]
        p_list = []
        for frac in frac_list:
            if frac == 0:
                continue
            else: 
                p_frac = frac * math.log2(frac)
                p_list.append(p_frac)
        entropy = -1*(sum(p_list))
        entropy = (f'{entropy:.2f}')
        sorted_dict[kmer].append(entropy)
        # print(entropy)
    # print(sorted_dict)
            
    count = 0
    for kmer in sorted_dict:
        count += 1
        print(f'{kmer}: {sorted_dict[kmer][0]}\t{sorted_dict[kmer][1]}')
        if count >= num_top_kmers_show:
            break
    # print(count)

   ## printing the num top kmers to show
    # top_kmers_show = sorted_keys[0:num_top_kmers_show]
    
    # for kmer in top_kmers_show:
    #     print("{}: {}".format(kmer, sorted_dict[kmer][0], sorted_dict[kmer][1]))

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()