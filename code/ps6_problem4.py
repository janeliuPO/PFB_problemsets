#!/usr/bin/env python3
import sys

#want to open and read contents of a FASTQ file with sequences
#format of file is @seq_id\nsequence\n+\nASCII.
#count and report total number of lines
#count and report total number of sequence IDs
#count and report total number of characters
#count and report total number of nucleotides
#average line length of all the lines
#average line length of the lines that contain sequences
#then print each line

line_count = 0
with open("Python_06.fastq.txt","r") as text_read:
    for line in text_read: #read each line
        line_count = line_count +1 #count each line

print(f'The total number of lines in this file is {line_count}.')


#1, 5, 9,
#4, 8, 12
seqID_count = 0
with open("Python_06.fastq.txt","r") as text_read:
    for line in text_read:
        line_count = line_count +1 #count each line
        if (line_count + 3)%4 == 0: #only want lines that have SeqID
            seqID_count = seqID_count + 1 #count each SeqID

print(f'The total number of sequence IDs is {seqID_count}.')

#2, 6, 10
#2-1+3
total_nts = 0
total_nt_lines = 0
with open("Python_06.fastq.txt","r") as text_read:
    for line in text_read:
        line_count = line_count +1 #count each line
        if (line_count - 1 + 3)%4 == 0: #only want lines that have nt seq
            total_nt_lines = total_nt_lines +1 #total number of lines ith nt
            nt_count = len(line)
            total_nts += nt_count #count each nt
    avg_ntlength = total_nts/total_nt_lines
        
print(f'The average length of the lines that contain sequences in this file is {avg_ntlength}.')

total_line_lenght = 0
with open("Python_06.fastq.txt","r") as text_read:
    for line in text_read:
        line_count = line_count +1 #count each line
        line_length = len(line)
        total_line_lenght += line_length
    avg_length = total_line_lenght/line_count
        
print(f'The average length of the lines in this file is {avg_length}.')