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

args = parser.parse_args()

flow_cell_names = args.flow_cell_names
flow_cells = args.flow_cells
lanes = args.lanes
samples = args.sample_ids
index = args.index

samples = samples.split(".")

flow_cells = flow_cells.split(".")

lanes = lanes.split(".")

flow_cell_names = flow_cell_names.split(".")

index = index.split(".")

d = {}
if len(flow_cell_names) == 1:
    flow_cell_names = "".join(flow_cell_names)
    for s, f, l,  i in zip(samples, flow_cells, lanes,index):
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
    for s, f, n,l, i in zip(samples, flow_cells, flow_cell_names, lanes, index, ):
        index_split = i.split(",")
        if len(index_split) == 2:
            index2=index_split[1]
            i = index_split[0]
            
        else:
            index2="."
        
        l =  ",".join(list(l))
        sample_id =  [s,f,n, l, i, index2]
        d[s] = sample_id
    
    
data = pd.DataFrame.from_dict(d, orient='index', columns=["id","flowcell_number","flowcell_name","lane_numbers","index", "index2"])

data.to_csv("mkfastq_samples.tsv",sep='\t', index=False)
    
        
