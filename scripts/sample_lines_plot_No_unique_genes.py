#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:24:30 2022

@author: patrice.zeis
"""
import numpy as np
import pandas as pd
import statistics
import subprocess
import matplotlib.pyplot as plt
from collections import Counter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--samplemax", help="number of samplings", type=int)
parser.add_argument("-l", "--samplelines", help="number of lines to sample", type=int)
parser.add_argument("-s", "--stripedsamfile", help="input stripped sam file")
parser.add_argument("-m", "--minnumber", help="min number of reads for a gene", type=int)

args = parser.parse_args()

sample_max = args.samplemax
file = args.stripedsamfile ### can be input for python script
sample = str(args.samplelines)
minnumber = args.minnumber

bashCommand = "shuf -n "+sample+" "+file
lst_sample_genes = []
count = 0
while (count < sample_max):
    process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE) 
    gene_ids = str(process)
    gene_ids = gene_ids.split("'")
    del gene_ids[0:9]
    gene_ids = gene_ids[0]
    gene_ids = gene_ids.split("\\n")
    del gene_ids[-1]
    gene_ids = ','.join(gene_ids).replace(';',',').split(",")
    gene_ids = ','.join(gene_ids).replace('GX:Z:','').split(",")
    values_genes = Counter(gene_ids).values()  
    values_genes = list(values_genes)
    values_genes  = np.array(values_genes)
    unique_genes = sum(values_genes >= minnumber)   
    lst_sample_genes.append(unique_genes)
    count = count + 1 
    
fig, ax1 = plt.subplots()
sds = round(statistics.pstdev(lst_sample_genes))
ax1.set_ylabel("unique_genes")
title = "No.genes_sampled_"+str(sample_max)+"x_from_"+sample+"_lines_of_sam: \n"+file.split(".sam")[0]+"_with_min"+str(minnumber)+"_of_reads_"+"SD="+str(sds)
ax1.set_title(title)
ax1.boxplot(lst_sample_genes)
filenam = "sampled"+str(sample_max)+"x_from_"+sample+"_lines_of_sam:"+file.split(".sam")[0]+"_with_min"+str(minnumber)+"_of_reads_"+".png"
plt.savefig(filenam)
