
Reference: ([Chapter 3 How do we assemble genomes?](https://www.bioinformaticsalgorithms.org/bioinformatics-chapter-3))

# 3.2 The String Reconstruction Problem

Given a string Text, its k-mer composition Compositionk(Text) is the collection of all k-mer substrings of Text (including repeated k-mers). For example,

Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}.

### Coding Challenges 3.2.1: Generate the k-mer composition of a string.

&nbsp;&nbsp;&nbsp;&nbsp;__Input__: An integer k and a string Text.

&nbsp;&nbsp;&nbsp;&nbsp;__Output__: Compositionk(Text), where the k-mers are arranged in lexicographic order.

[k-mer generator](k-mer_generator.py)

However, reconstruct string from k-mers is complicated, especially there are repeats in the genome

# 3.3 String Reconstruction as a Walk in the Overlap Graph

### Code Challenge 3.3.1: Solve the String Spelled by a Genome Path Problem.
The answer is different, need to review <font color = "red">(not yet finished)</font>

[path_to_genome](/stringReconstitute/pathToGenome.py)

# 3.4 Another Graph for String Reconstruction
## Gluing nodes and de Bruijn graphs

3-mer as node -> Assign 3-mer to edges: see below example

__1. 3-mer into edges, and prefix of 3-mer as node__

<figure>
    <img src="./pic/3.4.1merAsEdge.png" alt="3-mer as edge">
    <figcaption>Figure 3.4.1: 3-mer as edge instead of node.</figcaption>
</figure>

<figure>
    <img src="./pic/3.4.2merAsEdge.png" alt="3-mer as edge">
    <figcaption>Figure 3.4.2: 3-mer with prefix (first 2 mer, k-1 mer) as node.</figcaption>
</figure>

__2. Gluing identical nodes__

<figure>
    <img src="./pic/3.4.3gluingNodes_1.png" alt="3-mer as edge">
    <figcaption>Figure 3.4.3: Gluing identical node (AT) into one node.</figcaption>
</figure>


<figure>
    <img src="./pic/3.4.4gluingNodes_2.png" alt="3-mer as edge">
    <figcaption>Figure 3.4.4: Gluing identical node (TG) into one node.</figcaption>
</figure>

<figure>
    <img src="./pic/3.4.5gluingNodes_3.png" alt="3-mer as edge">
    <figcaption>Figure 3.4.5: Gluing identical node (GG) into one node.</figcaption>
</figure>

Resulting graph: __de Bruijn graph__

de Bruijn graph of TAATGCCATGGGATGTT

    denoted DeBruijn3(TAATGCCATGGGATGTT)
1. number of nodes: 16 -> 11
2. number of edges are the same as original one


In general, given a genome Text, PathGraphk(Text) is the path consisting of __|Text| - k + 1 edges__, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text. 

__The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).__

### Code Challenge 3.4.1: Solve the De Bruijn Graph from a String Problem.


&nbsp;&nbsp;&nbsp;&nbsp;__Input__: An integer k and a string Text.

&nbsp;&nbsp;&nbsp;&nbsp;__Output__: DeBruijnk(Text), in the form of an adjacency list.

<font color = "red">I felt like I didn't do well for the challenge, can be re-checked</font>

[deBruijnk challenge to generate adjacent matrix](./stringReconstitute/deBruijnk.py)

STOP and Think: Consider the following questions.

1. If we gave you the de Bruijn graph DeBruijnk(Text) without giving you Text, could you reconstruct Text?

2. Construct the de Bruijn graphs DeBruijn2(TAATGCCATGGGATGTT), DeBruijn3(TAATGCCATGGGATGTT), and DeBruijn4(TAATGCCATGGGATGTT). What do you notice?

3. How does the graph DeBruijn3(TAATGCCATGGGATGTT) compare to DeBruijn3(TAATGGGATGCCATGTT)?


# Walking in the de Bruijn Graph

## Eulerian path

<figure>
    <img src="./pic/3.5.1deBruijnkPath.png" alt="3-mer as edge">
    <figcaption>Figure 3.5.1: The path from TA to TT spelling out the genome TAATGCCATGGGATGTT has become “tangled" in the de Bruijn graph. The numbering of the fifteen edges of the path indicates an Eulerian path reconstructing the genome.</figcaption>
</figure>

String Reconstruction Problem --> __finding an Eulerian path in the de Bruijn graph__. 

    constructing this graph requires us to know the correct ordering of the k-mers in Text!


STOP and Think: Can you construct DeBruijnk(Text) if you don’t know Text but you do know its k-mer composition?

## Another way to construct de Bruijn graphs

__CompositionGraph3(TAATGCCATGGGATGTT)__ 
    
    3-mer composition of TAATGCCATGGGATGTT

Each 3-mer is assigned to a directed edge, with its prefix labeling the first node of the edge and its suffix labeling the second node of the edge

The edges of this graph are isolated, meaning that no two edges share a node.

<figure>
    <img src="./pic/3.5.2CompositionGraph.png" alt="3-mer as edge">
    <figcaption>Figure 3.5.2: CompositionGraph3(TAATGCCATGGGATGTT) representation </figcaption>
</figure>


STOP and Think: Glue identically labeled nodes in CompositionGraph3(TAATGCCATGGGATGTT). How does the resulting graph compare to DeBruijn3(TAATGCCATGGGATGTT)?
