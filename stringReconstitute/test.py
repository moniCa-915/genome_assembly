class Node:
    def __init__(self, read_start, read_end):
        self.content = read_start + "|" + read_end

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacent_list = {}
    
    def add_nodes(self, start, end):
        content = start + "|" + end
        if content not in self.nodes:
            self.nodes[content] = []
        self.nodes[content].append(Node(start, end))

def paired_dB(paired_read):
    paired_bBgraph = Graph()

    start = paired_read[0]
    start_prefix = start[: -1]
    start_suffix = start[1:]

    end = paired_read[1:]
    end_prefix = end[: -1]
    end_suffix = end[1:]

    print(start_prefix)

    paired_bBgraph.add_nodes(start_prefix, end_prefix)
    # paired_bBgraph.add_nodes(start_suffix, end_suffix)

if __name__ == "__main__":

    bottom =  "GCCATGGGATGTT"
    paired_ = ('TAA', 'CAA')

    paired_dB(paired_)

    

