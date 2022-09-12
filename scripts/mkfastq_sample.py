#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:50:02 2022

@author: patrice.zeis
"""

import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sample_ids", help="name of samples", type=str)
parser.add_argument("-l", "--lanes", help="give lanes", type=str)
parser.add_argument("-i", "--index", help="give index", type=str)
parser.add_argument("-f", "--flow_cells", help="give flowcells numbers(s)", type=str)
parser.add_argument("-n", "--flow_cell_names", help="give flowcells numbers(s)", type=str)
parser.add_argument("-m", "--multiomic_atac_index",nargs='?' , help="give_atac_index", type=str)

args = parser.parse_args()

flow_cell_names = args.flow_cell_names
flow_cells = args.flow_cells
lanes = args.lanes
samples = args.sample_ids
index = args.index
if args.multiomic_atac_index is not None:
    atac_index = args.multiomic_atac_index
    atac_index = atac_index.split(".") 

samples = samples.split(".")

flow_cells = flow_cells.split(".")

lanes = lanes.split(".")

flow_cell_names = flow_cell_names.split(".")

index = index.split(".")

#rna1 = "R" in layer
#rna2 = "r" in layer
#rna = rna1 | rna2

#atac1 = "A" in layer[0]
#atac2 = "a" in layer[0]
#atac = atac1 | atac2

#if rna | atac:
#
#    if rna:
#        layer = "RNA"
#    else:
#        layer = "ATAC"
#
d = {}
if len(flow_cell_names) == 1:
    flow_cell_names = "".join(flow_cell_names)
    if args.multiomic_atac_index is None:
        for s, f, l, i in zip(samples, flow_cells, lanes,index):
            index_split = i.split(",")
            if len(index_split) == 2:
                index2=index_split[1]
                i = index_split[0]
            
            else:
                index2="."

            l =  ",".join(list(l))
            sample_id =  [s,f,flow_cell_names, l, i, index2]
            d[s] = sample_id

    else:
        for s, f, l, i, m in zip(samples, flow_cells, lanes,index, atac_index):
            index_split = i.split(",")
            if len(index_split) == 2:
                index2=index_split[1]
                i = index_split[0]
            else:
                index2="."

            l =  ",".join(list(l))
            sample_id =  [s,f,flow_cell_names, l, i, index2, m]
            d[s] = sample_id


    
else:
    if args.multiomic_atac_index is None:
        for s, f, n,l, i in zip(samples, flow_cells, flow_cell_names, lanes, index ):
            index_split = i.split(",")
            if len(index_split) == 2:
                index2=index_split[1]
                i = index_split[0]
            
            else:
                index2="."
        
            l =  ",".join(list(l))
            sample_id =  [s,f,n, l, i, index2]
            d[s] = sample_id
    else:
        for s, f, n,l,i, m in zip(samples, flow_cells, flow_cell_names, lanes, index, atac_index):
            index_split = i.split(",")
            if len(index_split) == 2:
                index2=index_split[1]
                i = index_split[0]
            else:
                index2="."
            l =  ",".join(list(l))
            sample_id =  [s,f,n, l, i, index2, m]
    
    
data = pd.DataFrame.from_dict(d, orient='index', columns=["id","flowcell_number","flowcell_name","lane_numbers","index", "index2", "atac_index"])

data.to_csv("mkfastq_samples.tsv",sep='\t', index=False)
    
#else:
#    raise ValueError("If Atac layer give either 'ATAC', 'A', ','[Aa]tac' or 'a' and if RNA give either 'RNA', 'R', '[Rrna]' and 'r'")
