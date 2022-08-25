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
