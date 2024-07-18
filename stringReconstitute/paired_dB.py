class Node:
    def __init__(self, start_mer, end_mer):
        self.start_mer = start_mer
        self.start_mer = end_mer

class Graph:
    def __init__(self):
        self.graph = {}
        return 0
    
    def add_nodes(self, mer):
        return 0

def paired_reads(text, k , d):
    paired_dB = []
    for i in range(len(text) - d - 2 * k + 1):
        first_k_mer = text[i: i + k]
        last_k_mer = text[i + k + d: i + (2 * k) + d]
        paired_dB.append((first_k_mer, last_k_mer))
    print(paired_dB)
    print(sorted(paired_dB))

def paired_dB(first_mer, last_mer):
    dB_graph = {}
    dB_graph[first_mer].append(last_mer)
    return 0

if __name__ == "__main__":
    text = "TAATGCCATGGGATGTT"
    k = 3
    d = 1
    paired_reads(text, k, d)
    top = "TAATGCCATGGGA"
    bottom =  "GCCATGGGATGTT"

