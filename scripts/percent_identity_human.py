#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:45:11 2023

@author: patrice.zeis
"""

import re
import sys
import numpy as np
import pandas as pd

blastn = sys.argv[1]

peak_name = []
line_num = [] 

with open (blastn, "r") as input:         
    for count, line1 in enumerate(input):
        if bool(re.search('Query #', line1)):
            
            #### split based on #Query and save the peak information together with index 
            seq = line1.split("Query ")[1].split(": ")[1].split()[0]
            print(seq)
            print(count)
            peak_name.append(seq)
            line_num.append(count)


line_num_alignment = [] 

with open (blastn, "r") as input:         
    for count, line1 in enumerate(input):
        if bool(re.search('Alignments:', line1)):
            line_num_alignment.append(count)
            
            
output = blastn.split("/")
output = output[len(output)-1]
output = output.split(".txt")[0]
output = output.split("_")[0]
outputfile = output+"_Peaks_percent_human_identity.csv"

stepper = np.arange(0, len(line_num), 1).tolist()

percent_identity = []

for i in stepper:
    with open (blastn, "r") as input:
        peak_lines = input.readlines()[line_num[i]:line_num_alignment[i]]
        for n in peak_lines:
            if bool(re.search('Homo', n)):
                m = re.split("\s+", n)
                y = m[len(m)-4]
                percent_identity.append(y)
                break
                

d = {"Peaks":peak_name, "Per.Ident":percent_identity}
df = pd.DataFrame(d, columns=["Peaks", "Per.Ident"])            

df.to_csv(outputfile, index=False)
    
