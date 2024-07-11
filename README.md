# genome_assembly
capstone project of Data Structures and Algorithms Specialization

Two approaches
1. Overlap-Layout-Consensus (OLC) assembly
2. de Bruijn Graph (DBG) assembly

# Overlap Layout Consensus Assembly
Three steps as derived from its name
1. Overlap: build overlap graph
Building a directed graph where directed edges connect overlapping nodes

an overlap is a suffix/prefix match of >= 3 characters

a vertex is a read, a directed edge is an overlap between suffix of source and prefix of sink




