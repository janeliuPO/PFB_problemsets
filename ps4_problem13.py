#!/usr/bin/env python3
import sys

#define list
#for each element of the list
#lenghts_list = [len(element) for element in list]
#print lengths_list
#f string with list_length[index]\tlist[index]

list1 = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
sorted_list = sorted(list1, key=len, reverse = True)
print(sorted_list)

lengths_list = sorted([len(seq) for seq in sorted_list], reverse = True)
print(lengths_list)

for i in range(len(sorted_list)):
    print(f'{[i]}\t{lengths_list[i]}\t{sorted_list[i]}')