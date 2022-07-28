### @author: patrice.zeis

import gzip
import time
import sys
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted

start = time.time()

if len(sys.argv) != 3:
    raise ValueError("Please provide R1 fastq file as input and only R1 fastq file")
inputfile = sys.argv[1]
inputfile2 = sys.argv[2]
 
output = inputfile.split(".fastq.gz")    
outputfile = output[0]+"_reads.fastq" 


d = {}
f1 = 0 
with gzip.open (inputfile, "r") as input:
    for line1, line2, line3, line4 in zip(input, input, input, input):
        key = line2.decode("utf-8").split()[0][0:28]
        if key not in d.keys():
            d[key] = 1
        else:
            d[key] = d[key] + 1
        f1 = f1+1
        
        
f1_bcumi = len(d)

f2 = 0 
d2 = {}
with gzip.open (inputfile2, "r") as input:
    for line1, line2, line3, line4 in zip(input, input, input, input):
        key = line2.decode("utf-8").split()[0][0:28]
        if key not in d2.keys():
            d2[key] = 1
        else:
            d2[key] = d2[key] + 1
        f2 = f2+1
        
f2_bcumi = len(d2)

overlap = 0

if len(d) < len(d2):
    for key in d:
        if key in d2:
            overlap = overlap+1
else:
    for key in d2:
        if key in d:
            overlap = overlap+1
    
uni_d = len(d)-overlap
uni_d2 = len(d2)-overlap
        
        
venn2(subsets = (uni_d, uni_d2, overlap), set_labels = ("input_fastq_1" , "input_fast_2" ))
filenam = "overlap_BC_UMI_combination"+"_Fastq1:"+inputfile.split(".fastq.gz")[0]+"_Fastq2:"+inputfile2.split(".fastq.gz")[0]+".png"

plt.savefig(filenam)

end_time = time.time()
print(end_time - start)
