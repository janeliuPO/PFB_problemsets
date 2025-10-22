#!/usr/bin/env python3
import sys
import re
reDict_bionet = {}
#open and read the text line by line
file = open("bionet.txt","r")
content = file.readlines() #this allows me to limit the lines we read
    
for line in content[11:-1]:
    # print(line)
    line = line.rstrip()
    list = re.split(r" {4,}", line)
    # print(list)
    reName = list[0]
    # print(reName)
    site = list[1]
    reDict_bionet[reName] = site

# print(reDict_bionet)

if sys.argv[1] in reDict_bionet:
    print(f'Found it! The RE is {sys.argv[1]} and its site is {reDict_bionet[sys.argv[1]]}.')
    cut = reDict_bionet[sys.argv[1]].split('^')
    print(cut)
    start = cut[0]
    end = cut[1]
    with open(sys.argv[2],"r") as file_read:
        for line in file_read:
            line = line.rstrip()
            # print(line)
            if not line.startswith('>'):
                new_re = f'{cut[0]}^{cut[1]}'
                print(new_re)
                new_line = re.sub(r"(cut[0])(cut[1])", new_re, line)
                print(new_line)

# cuts = new_fasta.split('^')
# print(cuts)
            # if re.search(r">", line):
    #             for found in re.finditer(r">(\S+.*)", line):
    #             seqID = found.group(1)
            # print(seqID)
#             fastaDict_re[seqID] = ''
#             else: 
#             fastaDict_re[seqID] += line
        
        


