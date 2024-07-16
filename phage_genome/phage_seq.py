# Construct an overlap graph: two reads are joined by a directed edge of weight equal to the length of the maximum overlap of these two reads.

class Node:
    def __init__(self, content):
        self.content = content

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edge = []
        self.adjacent_list = {}
    
    def add_node(self, content):
        if content not in self.nodes:
            self.nodes[content] = Node[content]
            self.adjacent_list[content] = []

    def add_edges(self, start, end):
        if start in self.nodes and end in self.nodes:
            start_node = self.nodes[start].content
            end_node = self.nodes[end].content
            self.edge.append(Edge(start_node, end_node))
            self.adjacent_list[start_node].append(end_node)


# construct a graph with directed eges
def addEdge(source, sink):
    
    return 0

if __name__ == "__main__":
    test_pattern = ["AAC", "ACG", "GAA", "GTT", "TCG"]
    k = 2


    # test code
    # read1 = "CTCGGCTCTAGCCCCTCATTTT" # source
    # read2 = "GGCTCTAGGCCCTCATTTTTT" # sink
    # suffix of source is similar to prefix of sink

    # driver code
    # with open("reads.txt", "r") as file:
    #     reads = file.readlines()
    #     for read in reads:
    #         print(read)




