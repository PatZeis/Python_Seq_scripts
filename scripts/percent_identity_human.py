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

with open (blastn, "r") as input:
    total_lines = sum(1 for line in input)
    
            
            
output = blastn.split("/")
output = output[len(output)-1]
output = output.split(".txt")[0]
output = output.split("_")[0]
outputfile = output+"_Peaks_percent_human_identity_query_coverage.csv"


stepper = np.arange(0, len(line_num), 1).tolist()

line_num.append(total_lines)

percent_identity = []
query_coverage = []
query_identity = []

for i in stepper:
    with open (blastn, "r") as input:
        peak_lines = input.readlines()[line_num[i]:line_num[i+1]]
        for count, n in enumerate(peak_lines):
            if bool(re.search('Homo', n)):
                m = re.split("\s+", n)
                y = m[len(m)-4]
                z = m[len(m)-6]
                z1 = int(float(y))*(int(float(z.replace("%", "")))/100)
                query_identity.append(z1)
                percent_identity.append(y)
                query_coverage.append(z)
                
                break
            
            if count == len(peak_lines)-1:
                percent_identity.append(0)
                query_identity.append(0)
                query_coverage.append(0)
                                
    if i == len(stepper)-1:
        break


d = {"Peaks":peak_name, "Per.Ident":percent_identity}
d1 = {"QueryCover":query_coverage, "QueryIdentity":query_identity}

df = pd.DataFrame(d, columns=["Peaks", "Per.Ident"])            
df1 = pd.DataFrame(d1, columns=["QueryCover", "QueryIdentity"])

df = pd.concat([df, df1 ], axis=1)
 
df.to_csv(outputfile, index=False)
          
