#!/usr/bin/env python

import sys, re

# open file
# remove newline characters
# skip lines with # as first chracter
# split lines at \t
# save the data into a dictionary - matrix is key, with values are percid, alen, and evaule - dictionary of lists!!
# close file, move on...
if (len(sys.argv) < 5):
    print("# " + " ".join(sys.argv))
else:
    print("# " + " ".join(sys.argv[0:5]) + ' ...')

def search_results(file):
    this_data_dict = {}
    with open(file, "r") as read:
        for line in read:
            line = line.rstrip()
            if not line.find('#') == 0:
                columns = re.split(r"\t", line)
                if 'qseqid' not in this_data_dict:
                    #when building dict, good to use this if statement
                    this_data_dict['filename'] = file
                    this_data_dict['qseqid'] = columns[0]
                    this_data_dict['sseqid'] = columns[1]
                    this_data_dict['percid'] = columns[2]
                    this_data_dict['alen'] = columns[3]
                    this_data_dict['mismat'] = columns[4]
                    this_data_dict['gaps'] = columns[5]
                    this_data_dict['q_start'] = columns[6]
                    this_data_dict['q_end'] = columns[7]
                    this_data_dict['s_start'] = columns[8]
                    this_data_dict['s_end'] = columns[9]
                    this_data_dict['evalue'] = columns[10]
                    this_data_dict['bits'] = columns[11]
                else:
                    continue


    return this_data_dict

# to iterate through many input files:
# for file in sys.argv[1:]:
# data = search_results(file)

file_name_1 = sys.argv[1] + '_BLOSUM62'
file_name_2 = sys.argv[2] + '_BLOSUM80'
file_name_3 = sys.argv[3] + '_PAM30'
file_name_4 = sys.argv[4] + '_PAM70'


dict_1 = search_results(sys.argv[1])
dict_2 = search_results(sys.argv[2])
dict_3 = search_results(sys.argv[3])
dict_4 = search_results(sys.argv[4])

# print(f'For {file_name_1}, the dictionary is: {dict_1}')

#build dictionary with matrix name as key
mydict = {'BLUSUM62': dict_1, 'BLOSUM80': dict_2, 'PAM30': dict_3, 'PAM70': dict_4}

# print(mydict['BLOSUM80']['percid'])
# print(mydict)

# print out the values percid, alen, and evalue - those are [2] [3] and [10]
with open("blast_analysis.txt", "a") as blast_file:
    blast_file.write(f'\nAnalysis with blast_rand5-200:\n{"Matrix": ^10}\t{"% ID": ^10}\t{"alen": ^10}\t{"evalue":}\n')
    for matrix in mydict:
        blast_file.write(f'{matrix: ^10}\t{mydict[matrix]['percid']: ^10}\t{mydict[matrix]['alen']: ^10}\t{mydict[matrix]['evalue']}\n')