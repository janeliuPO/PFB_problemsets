#!/usr/bin/env python
import os, sys

## method: sequence_to_kmer_list(sequence, kmer_length)
##
##  Extracts all kmers of a specified length from a sequence
##
##  ie.  sequence: GATCGATCGATCGA
##   and given kmer_length = 4
##   would yield
##                 GATC
##                  ATCG
##                   TCGA
##                    .... and so forth
##                       
##  input parameters:
##
##  sequence : nucleotide sequence (type: string)
##
##  returns kmer_list : list of kmer sequences.
##                    ie.  ["GATC", "ATCG", ...]
    
def sequence_to_kmer_list(sequence, kmer_length):

    kmers_list = list()

    # sequence is from seq_list

    ## begin your code
    uppseq = sequence.upper()
    
    for x in range(0, len(uppseq)-kmer_length):
        kmer = uppseq[x:x+kmer_length]
        kmers_list.append(kmer)


    
    ## end your code

    return kmers_list

##some code for testing
# sequence = 'aattggaa'
# kmer_length = 3
# print(sequence_to_kmer_list(sequence, kmer_length))

def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} sequence kmer_length\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    sequence = sys.argv[1]
    kmer_length = int(sys.argv[2])

    kmers  = sequence_to_kmer_list(sequence, kmer_length)

    print(kmers)

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    