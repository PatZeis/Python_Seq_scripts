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
