from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.vertices = num_vertices
        self.graph = defaultdict(list)
        self.IN = [0] * self.vertices
        self.verticesList = []
    def addEdge(self, start, end):
        self.graph[start].append(end)
        self.verticesList.append(start)
        self.verticesList.append(end)

def deBruijn(Patterns, k):
    deBruijnGraph = Graph(len(Patterns) * 2)
    for pattern in Patterns:
        prefix = pattern[: (k - 1)]
        suffix = pattern[1:]
        deBruijnGraph.addEdge(prefix, suffix)
    return deBruijnGraph

def DFSUtil(start_vertex, graph, visited):
    visited[start_vertex] = True
    for neighbor in graph[start_vertex]:
        if visited[neighbor] == False:
            DFSUtil(neighbor, graph, visited)
    return 0

def EulerianPath(dBGraph, verticesList):
    # graph is strongly connected components
    visited = {key: False for key in verticesList}
    start_vertex = -1
    for vertex in dBGraph:
        if dBGraph[vertex]:
            start_vertex = vertex
            break
    
    # depth first search
    DFSUtil(start_vertex, dBGraph, visited)
    
    # each vertex has same INdegree and OUTdegree (balanced)
    return 0

def stringConstruct(Patterns):
    
    return 0

if __name__ == "__main__":
    k = 4

    patterns = ["CTTA",
                "ACCA",
                "TACC",
                "GGCT",
                "GCTT",
                "TTAC"]

    graph = {'CTT': ['TTA'], 'ACC': ['CCA'], 'TAC': ['ACC'], 'GGC': ['GCT'], 'GCT': ['CTT'], 'TTA': ['TAC']}
    testGraph = deBruijn(patterns, k)
    print(testGraph.graph)
    vertices_list = testGraph.verticesList
    EulerianPath(graph, vertices_list)

# GGCTTACCA