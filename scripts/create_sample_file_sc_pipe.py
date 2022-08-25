#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:22:00 2022

@author: patrice.zeis
"""

import pandas as pd
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--flow_cells", help="give flowcells numbers(s)", type=str)
parser.add_argument("-l", "--lanes", help="give lanes", type=str)
parser.add_argument("-s", "--sample_ids", help="name of samples", type=str)

args = parser.parse_args()

flow_cells = args.flow_cells
lanes = args.lanes
samples = args.sample_ids

samples = samples.split(".")

flow_cells = flow_cells.split(".")
flow_cells2 = []
for i in flow_cells:
    flow_cells2.append(";".join(i.split(",")))

lanes = lanes.split(".")
lanes2 = []

for i in lanes:
    lanes_samp = i.split(",")
    lanes_out = []
    for n in lanes_samp:
        lanes_out.append(",".join(np.array(["00"+str(x) for x in list(n)])))
                                
    lanes2.append(";".join(lanes_out))

species_id = "macaca_fascicularis"
reference_id = "Macaca_mulatta.Mmul_10.101"
mito = "MT-"

sample_ids = np.array([x+"\t"+species_id+"\t"+reference_id+"\t"+mito+"\t"+y+"\t"+z  for x, y, z in zip(samples, flow_cells2, lanes2)])

d = {}
for i,y in zip(samples,sample_ids):
    d[i] = y.split("\t") 

data = pd.DataFrame.from_dict(d, orient='index', columns=["id","species-id","reference-id","mitochondrial-genes","flowcells", "lanes"])

data.to_csv("samples.tsv",sep='\t', index=False)
    


