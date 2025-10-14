#!/usr/bin/env python3
import sys

peptide_seq = sys.argv[1] #this is the input peptide sequence
total_count = len(peptide_seq) #length of total peptide  
print(f"Total number of amino acids in '{peptide_seq}' : {total_count}")

nonpolar_to_count = ['A', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W'] #counts for nonpolar amino acids
nonpolar_count = sum(1 for char_in_string in peptide_seq if char_in_string in nonpolar_to_count)
print(f"Total count of nonpolar in '{peptide_seq}': {nonpolar_count}")

percent_nonpolar = int((nonpolar_count/total_count)*100)
print(f"Percent hydrophobic in '{peptide_seq}' : {percent_nonpolar}")


