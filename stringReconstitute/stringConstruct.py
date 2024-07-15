from collections import defaultdict

class Node:
    def __init__(self, content):
        self.content = content
        self.INdegree = 0
        self.OUTdegree = 0

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Graph:
    def __init__(self):
        self.nodes ={}
        self.edges = []
        # add for checking SCC
        self.adjacent_list = {}

    def add_node(self,content):
        if content not in self.nodes:
            self.nodes[content] = Node(content)
            self.adjacent_list[content] = []

    def add_edge(self, start_content, end_content):
        if start_content in self.nodes and end_content in self.nodes:
            start_node = self.nodes[start_content]
            end_node = self.nodes[end_content]
            self.edges.append(Edge(start_node, end_node))
            start_node.OUTdegree += 1
            end_node.INdegree += 1
            self.adjacent_list[start_content].append(end_content)

    # need to delete print function
    def isBalanced(self):
        for node in self.nodes.values():
            if node.INdegree != node.OUTdegree:
                ####
                print(node.content)
                ###
                return False
        return True

    def is_strongly_connected(self):
        # perform depth first search
        # create iterator
        iterator = iter(self.nodes)
        start_node = next(iterator)
        visited = {node: False for node in self.nodes}
        
        def DFS(vertex):
            visited[vertex] = True
            for neighbor in self.adjacent_list[vertex]:
                if not visited[neighbor]:
                    DFS(neighbor)
        DFS(start_node)

        if not all(visited.values()) == True:
            return False
        
        # check if all nodes can reach the starting node (transpose graph)
        transpose_adj_list = 

    def print_graph(self):
        for edge in self.edges:
            print(f"{edge.start.content} -> {edge.end.content}")
    

def deBruijn(patterns):
    dBGraph = Graph()
    for pattern in patterns:
        prefix = pattern[: (k - 1)]
        suffix = pattern[1:]
        dBGraph.add_node(prefix)
        dBGraph.add_node(suffix)
        dBGraph.add_edge(prefix, suffix)
    dBGraph.print_graph()
    return dBGraph



if __name__ == "__main__":
    k = 4

    patterns = ["CTTA",
                "ACCA",
                "TACC",
                "GGCT",
                "GCTT",
                "TTAC"]
    
    dB = deBruijn(patterns)
    print(dB.isBalanced())
    print(dB.is_strongly_connected())

# GGCTTACCA