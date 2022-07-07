#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 10:42:24 2022

@author: patrice.zeis
"""

import sys
import re
if len(sys.argv) != 2:
    raise ValueError("Please provide SAm file as input")
inputfile = sys.argv[1]


output = inputfile.split(".sam")
outputfile = output[0]+"_stripped.sam"

output_file = open(outputfile, "w")
with open (inputfile, "r") as input:
    for line in input:
        if line[0] != "@":
            if "GX:Z:" in line:
                line1 = line.split("\t")
                matching = [s for s in line1 if "GX:Z" in s]
                line2 = "\t".join(matching)
                output_file.write(line2+"\n")
                #output_file.write(line)

output_file.close()
