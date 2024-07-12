Reference: ([Chapter 3 How do we assemble genomes?](https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-3))

# 3.2 The String Reconstruction Problem

Given a string Text, its k-mer composition Compositionk(Text) is the collection of all k-mer substrings of Text (including repeated k-mers). For example,

Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}.

## Coding Challenges 3.2.1: Generate the k-mer composition of a string.

&nbsp;&nbsp;&nbsp;&nbsp;__Input__: An integer k and a string Text.

&nbsp;&nbsp;&nbsp;&nbsp;__Output__: Compositionk(Text), where the k-mers are arranged in lexicographic order.

[k-mer generator](k-mer_generator.py)

However, reconstruct string from k-mers is complicated, especially there are repeats in the genome

# 3.3 String Reconstruction as a Walk in the Overlap Graph

## Code Challenge 3.3.1: Solve the String Spelled by a Genome Path Problem.
The answer is different, need to review

[path_to_genome](stringReconstitue/pathToGenome.py)

# 3.4 Another Graph for String Reconstruction
## Gluing nodes and de Bruijn graphs

3-mer as node -> Assign 3-mer to edges




