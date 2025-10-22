#!/usr/bin/env python3
import sys

taxa_string = sys.argv[1] #alows us to input text that we want to make list from.

print(taxa_string)

list_taxa = taxa_string.split(' : ') # this should make that input into a list

print(f'The list is: {list_taxa}') #put variables in {}
print(f'The type of this string is: {type(taxa_string)}')

print(f'The second item in this list is: {list_taxa[1]}')

print(f'The list, sorted alphabetically, is: {sorted(list_taxa)}')

#below, trying to sort the list by length of each string....
sorted_taxa = sorted(list_taxa, key=len)      
print(f'Sorted list: {sorted_taxa}')

