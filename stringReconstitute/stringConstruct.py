from collections import defaultdict

def DFS(start_vertex, adjacent_list, visited):
    visited[start_vertex] = True
    for neighbor in adjacent_list[start_vertex]:
        if not visited[neighbor]:
            DFS(neighbor, adjacent_list, visited)

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
        num_start_node = 0
        num_end_node = 0
        for node in self.nodes.values():
            if node.INdegree - node.OUTdegree == 1:
                num_end_node += 1
            elif node.OUTdegree - node.INdegree == 1:
                num_start_node += 1
            elif node.INdegree != node.OUTdegree:
                ####
                print(node.content)
                print(node.INdegree)
                print(node.OUTdegree)
                ###
                return False
        return (num_start_node == 1 and num_end_node == 1) or (num_start_node == 0 and num_end_node == 0)

    def is_strongly_connected(self):
        # perform depth first search
        # create iterator
        iterator = iter(self.nodes)
        start_node = next(iterator)
        visited = {node: False for node in self.nodes}
        print(start_node)

        DFS(start_node, self.adjacent_list, visited)
        print("SCC: " + str(all(visited.values())))
        print(visited)
        
        if not all(visited.values()):
            
            return False
        
        # check if all nodes can reach the starting node (transpose graph)
        transpose_adjacent_list = {node: [] for node in self.nodes}
        for node, neighbors in self.adjacent_list.items():
            for neighbor in neighbors:
                transpose_adjacent_list[neighbor].append(node)
        
        visited = {node: False for node in self.nodes}
        DFS(start_node, transpose_adjacent_list, visited)
        print("SCC: " + str(all(visited.values())))
        return all(visited.values())

    def find_eulerian_path(self):
        if not self.isBalanced() or not self.is_strongly_connected():
            print("no eulerian path")
            return None
        
        start_node = next((node.content for node in self.nodes.values() if node.OUTdegree - node.INdegree == 1), None)
        if not start_node:
            start_node = next(iter(self.nodes))        
        
        path = []
        stack = [start_node]

        while stack:
            u = stack[-1]
            if self.adjacent_list[u]:
                v = self.adjacent_list[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())
        path.reverse()
        return path

    def print_graph(self):
        for edge in self.edges:
            print(f"{edge.start.content} -> {edge.end.content}")
    
# delete print function
def deBruijn(patterns, k):
    dBGraph = Graph()
    for pattern in patterns:
        prefix = pattern[: (k - 1)]
        suffix = pattern[1:]
        dBGraph.add_node(prefix)
        dBGraph.add_node(suffix)
        dBGraph.add_edge(prefix, suffix)
    ####
    dBGraph.print_graph()
    print(dBGraph.adjacent_list)
    ###
    return dBGraph

def reconstruct_string_from_path(path, k):
    sequence = path[0]
    for node in path[1:]:
        sequence += node[-1]
    return sequence


if __name__ == "__main__":
    # k = 4

    # patterns = ["CTTA",
    #             "ACCA",
    #             "TACC",
    #             "GGCT",
    #             "GCTT",
    #             "TTAC",
    #             "TACG"]
    
    # dB = deBruijn(patterns, k)
    # print(dB.isBalanced())
    # print("if strongly connected: ")
    # print(dB.is_strongly_connected())
    # print(dB.find_eulerian_path())
    
    k = 4
    patterns = [
        "AAGC",
        "AGCT",
        "GCTG",
        "CTGA",
        "TGAA",
        "GAAG"
    ]

    dB = deBruijn(patterns, k)
    if dB.isBalanced() and dB.is_strongly_connected():
        eulerian_path = dB.find_eulerian_path()
        if eulerian_path:
            result = reconstruct_string_from_path(eulerian_path, k)
            print(f"Reconstructed string: {result}")
        else:
            print("No Eulerian path found.")
    else:
        print("Graph is not balanced or not strongly connected.")

    # patterns = []
    # with open("patterns.txt", "r") as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         patterns.append(line.strip())
    # k = 15
    # dB = deBruijn(patterns)
    # print(dB.isBalanced())

    # patterns = ["AAC", "ACG", "GAA", "GTT", "TCG"]
    # ACGTTCGA
    # k = 3
    # dB = deBruijn(patterns, k)
    # print(dB.isBalanced())


# GGCTTACCA