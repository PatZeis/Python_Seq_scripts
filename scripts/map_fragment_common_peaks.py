#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 16:24:41 2022

@author: patrice.zeis
"""

import gzip
import sys
import numpy as np 
import pandas as pd
from itertools import compress
from collections import Counter
import time
import argparse
import scipy.sparse as sparse
import scipy.io as sio

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fragment_path", help="path to fragment file")
parser.add_argument("-p", "--combined_peak_path", help="path to combined peaks")
parser.add_argument("-c", "--barcode_path", help="path to non empty barcodes")

args = parser.parse_args()

fragment_path = args.fragment_path
combined_peak_path = args.combined_peak_path
barcode_path = args.barcode_path

barcodes = {}

with gzip.open (barcode_path, "r") as bc:
    for line in bc:
        line2 = line.decode("utf-8")
        line2 = line2.split("\n")[0]  
        barcodes[line2] = ""


x = pd.read_csv(combined_peak_path, index_col=0)
chromosomes = x['seqnames'].unique()
d = {}
for i in chromosomes:
    print(i)
    chr_filt = x[x["seqnames"] == i]
    starts = chr_filt["start"].to_numpy() # .tolist()
    ends = chr_filt["end"].to_numpy() #.tolist()
    peak_names = np.array([i+":"+str(x)+"-"+str(y) for x, y in zip(starts, ends)])
    d[i] = { "starts": starts, "ends": ends, "peak_names": peak_names }


fragment = fragment_path

start2 = time.time()
cells = {}
with gzip.open (fragment, "r") as input:
    for line in input:
        start = time.time()
        line2 = line.decode("utf-8")
        if line2[0] != "#":
            line3 = line2.split("\t")
            chr = line3[0]
            if chr in chromosomes:
                barcode = line3[3]
                if barcode in barcodes.keys():
                    fragment_start = line3[1]
                    fragment_end = line3[2]
                    count = int(line3[4])
            
                    peak_starts = d[chr]["starts"]
                    peak_ends = d[chr]["ends"]
                    peaks = d[chr]["peak_names"]
            
                    left1 = peak_starts >= int(fragment_start)
                    left2 = peak_starts <= int(fragment_end)
                    right1 = peak_ends >= int(fragment_start)
                    right2 = peak_ends <= int(fragment_end)
                    mid1 = peak_starts <= int(fragment_start)
                    mid2 = peak_ends >= int(fragment_end)
            
                    left = np.logical_and(left1, left2)
                    right = np.logical_and(right1, right2)
                    mid = np.logical_and(mid1, mid2)
            
                    gene_names = peaks[left | right | mid]
                    gene_names = '|'.join(gene_names)
            
                    if len(gene_names) != 0:
                
                        if barcode not in cells.keys():
                            cells[barcode] = {}                              
                        if gene_names not in cells[barcode].keys():
                            cells[barcode][gene_names] = count
                        else:
                            cells[barcode][gene_names] = cells[barcode][gene_names] + count
                
                    end_time = time.time()
                    print(end_time - start)

                    
end_time2 = time.time()
print(end_time2 - start2)

cells2 = cells.copy()

for key in cells2.keys():
    start = time.time()
    cells2[key] = pd.DataFrame.from_dict(cells2[key], orient='index', columns=[key])
    end = time.time()
    print(end - start)

df = pd.concat([cells2[values] for values in cells2.keys()], axis=1) 
df = df.fillna(0)
sparse_matrix = sparse.csr_matrix(df)
sio.mmwrite("sparse_matrix.mtx",sparse_matrix)
peaks=df.index.values.tolist()
peaks = pd.DataFrame (peaks, columns = ['peaks'])
peaks.to_csv("common_peaks.csv")
cells = df.columns.tolist()
cells = pd.DataFrame (cells, columns = ['cells'])
cells.to_csv("barcodes.csv")
