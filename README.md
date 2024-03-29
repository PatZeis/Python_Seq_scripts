# Python scripts to process and analyze sequencing data files and reference files

## example to test how many genes are mapped in given number of reads starting from cellranger/STAR output 
##### bam to sam conversion 
``` bash
zeis@example:~$ samtools view -h -o GEX.sam gex_possorted_bam.bam
```
##### extract geneIDs of reads which mapped to a gene
``` bash
zeis@example:~$ python ~/python_scripts/extract_mapped_reads.py GEX.sam
```
##### Sample -i times -l number of reads mapping to a gene and plot number of genes with at least -m number of reads per gene for -s stripped file.sam 
``` bash  
zeis@example:~$ python ~/python_scripts/sample_lines_plot_No_unique_genes.py -i 10 -l 1000000 -m 5 -s GEX_stripped.sam
```

## test overlap of Barcode and UMI combination between two R1.fastq.gz files
##### combine fastq files from different lanes
``` bash 
zeis@example:~$ cat lane1_run1_R1.gz lane2_run1_R1.gz lane3_run1_R1.gz > run1_R1_fastq.gz
zeis@example:~$ cat lane1_run2_R1.gz lane2_run2_R1.gz lane3_run2_R1.gz > run2_R1_fastq.gz
```

##### run script looking for overlap of Barcode and UMI and plots overlap as Venn diagram 
``` bash
zeis@example:~$ python ~/python_scripts/check_umibarcode_overlap_2_fastq.py run1_R1_fastq.gz run2_R1_fastq.gz
``` 

##### run script to create sample input file for pipeline
``` bash
zeis@example:~$ python ~/python_scripts/create_sample_file_sc_pipe.py -s sample1.sample2.sample3.sample -l 12.12.12.12 -f 1.1.1.1

```

##### run script to create mkfastq sample input file for cellranger-arc mkfastq
 
``` bash
zeis@example:~$ python ~/python_scripts/mkfastq_sample.py -s samp1.samp2.samp3.samp4 -l 12.12.12.12 -i S1-A1.S1-A2.S1-A3.S1-A4 -f 1.1.1.1 -n flowcell_nam
```
###### for novaseq demultiplexing requires two indexes which can be assigned using ","
``` bash
zeis@example:~$ python ~/python_scripts/mkfastq_sample.py -s samp1.samp2.samp3.samp4 -l 12.12.12.12 -i S1-TT-A1.S1-TT-A2.S1-TT-A3.S1-TT-A4.TTCTCGATGA,GTGCCCGACA -f 1.1.1.1 -n flowcell_nam -m SI-NA-H8.SI-NA-B9.SI-NA-C9.SI-NA-F10 -a flowcell_nam_atac      
```
##### run script to create config file for snakemake, takes output of mkfastq_sample.py as input
``` bash
zeis@example:~$ python ~/python_scripts/generate_config_clean.py -i mkfastq_samples.tsv -b buckets/zeis -w 3M-february-2018.txt -g "https://cf.10xgenomics.com/releases/cell-arc/cellranger-arc-2.0.2.tar.gz?Expires=1663040898&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1hcmMvY2VsbHJhbmdlci1hcmMtMi4wLjIudGFyLmd6IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjYzMDQwODk4fX19XX0_&Signature=FGQ3AOD0pcBaK19yLQ4SpyEzdpXImF~G1VxfDqib1TIo0sIVIlQANhjH~xpONeh1s38jprYU257B0YK76JPQT6m9lish8jGT1HsyuFgHSN9t4ADr3eaqopDBY8DJeTCSVbpZwgpFKzEiBxOc8JuXOZG0jxnUc2yyyt9Bh1e0aLYHRP5-CZu6uwxBMxhmEModQlj5CPFIQFHb2kj26sBhKpmzJeXgCTzjemXXDj5aXSKCxAvTIzDZh8fnT8mQkKEepkxR6U-bN0N6tm8xIzWlSx1bqtG7NOrm3RY2kYDFbky8PE-FtJ1bIK0vDWAGbHIPtOp-3jFVQIbG9yS9d~ee-Q__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"
``` 

## extract nucleotide base sequence of peaks from reference genome fasta
#### input of script is .csv peak file with peak information in first column and reference genome fasta
``` bash
zeis@example:~$ python ~/python_scripts/extract_sequence_of_enhancers.py /path/genome.fa /path/peaks.csv
```

## extract percentage of sequence idendity of first human sequence match from mega blast output
``` bash 
zeis@example:~$ python ~/python_scripts/percent_identity_human.py Megablast_output.txt
```
      	 
