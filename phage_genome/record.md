# Assignment 1
__Problem Introduction__

In this challenge, you will be given the task of performing Genome Assembly on a simulated 'error-free' sequencing dataset. 

__Problem Description__

Given a list of error-free reads, perform the task of Genome Assembly and return the circular genome from which they came. 

__Dataset__

Each of '1618 lines' of the input contains a single read, that is, a string over {A, C, G, T}. The reads are given to you in alphabetical order because their true order is hidden from you. 

Each read is '100 nucleotides' long and contains no sequencing errors. 

Note that you are not given the 100-mer composition of the genome, i.e., some 100-mers may be missing.


__Output__


Output the assembled genome on a single line.

__What to do__
Construct an overlap graph: two reads are joined by a directed edge of weight equal to the length of the maximum overlap of these two reads. 

Then construct a Hamiltonian path in this graph in a greedy fashion: for each read select an out-going edge of maximum weight. Then read a string spelled by this path. To avoid computing overlaps between all pairs of reads, you may want to first compute a list of all pairs of reads that share a 𝑘-mer (for, say, 𝑘 = 12).


## Steps

### Generate artificial reads
Genome length is 5386 bp

According to the description, input is 1618 lines of 100-mer reads.






