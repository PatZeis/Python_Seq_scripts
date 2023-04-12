#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:45:34 2023

@author: patrice.zeis
"""
    
import re
import sys

fasta = sys.argv[1]
csv = sys.argv[2]

seq_name = []
line_num = []

with open (fasta, "r") as input:         
    for count, line1 in enumerate(input):
        if bool(re.search('>[0-9]|>[0-9][0-9]|>MT|>X|>Y|>chr[0-9]|>chr[0-9][0-9]|>chrM|>chrX|>chrY', line1)):
            seq = ">".join(line1.split()).split(">")[1]
            seq_name.append(seq)
            line_num.append(count)
seq_name2 = []
for i in seq_name:
    seq_name2.append(i.replace("chr", ""))

seq_name = seq_name2
seq_name2 = []

output = csv.split("/")
output = output[len(output)-1]
output = output.split(".csv")[0]
output = output.split("_")
outputfile = output[8]+"_supergroup_peak_list_base_sequence.txt"
output_file = open(outputfile, "w")
print(outputfile + "\n")

with open(csv, "r") as csv: #, open (fasta, "r") as input:
    for line in csv:
        peak = line.split(",")[0]
        peak_chr = peak.split("-")[0]
        if "chr" in peak_chr:
            print("retrieving peak sequence of " + peak + "\n") 
            peak_chr = "".join(peak_chr.split("chr"))
            start = int(peak.split("-")[1])-1
            end = int(peak.split("-")[2])
            ind = seq_name.index(peak_chr)
            ind_next = ind+1
            startline=line_num[ind]+1
            endline=line_num[ind_next]
            print("read fasta sequence" + "\n")
            with open (fasta, "r") as input:
                sequence=input.readlines()[startline:endline]
                sequence = "".join("".join(sequence).split("\n"))
                print("filter read sequence" + "\n")
                sequence = sequence[start:end]
                print("write peak and it's read sequence" + "\n")
                output_file.write(">"+peak+"\n"+sequence+"\n")


output_file.close()
            
        
        
        
