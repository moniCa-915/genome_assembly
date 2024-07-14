from collections import defaultdict
class Node:
    def __init__(self, label):
        self.label = label
        self.IN = 0
        self.OUT = 0

class Graph:
    def __init__(self, num_vertices):
        self.vertices = num_vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, adjacentMatrix):
        for i in range(len(adjacentMatrix)):
            for j in range(len(adjacentMatrix[i])):
                if adjacentMatrix[i][j] == 1:
                    self.graph[i].append(j)
    
    def addTransposeEdge(self, start, end):
        self.graph[start].append(end)
    
    def DFSutil(self, start_vertex, visited):
        visited[start_vertex] = True
        for neighbor in self.graph[start_vertex]:
            if visited[neighbor] == False:
                self.DFSutil(neighbor, visited)

    def transpose(self):
        transposeGraph = Graph(self.vertices)
        for node in self.graph:
            for child in self.graph[node]:
                transposeGraph.addTransposeEdge(child, node)
        return transposeGraph

    def isSCC(self):
        visited = [False] * self.vertices

        start_vertex = -1
        # initiate enter vertex
        for v in range(self.vertices):
            if len(self.graph[v]) > 0:
                start_vertex = v
                break
        # conduct depth-first search
        self.DFSutil(start_vertex, visited)
        # check if visit all vertices
        if not all(visited) == True:
            return False
        
        # check reverse graph
        transposeGraph = self.transpose()
        visited = [False] * self.vertices

        start_vertex = -1
        for v in range(self.vertices):
            if len(transposeGraph[v]) > 0:
                break
        # conduct DFS
        transposeGraph.DFSutil(start_vertex, visited)
        if not all(visited) == True:
            return False
        
        return True

    def isEulerian(self, graph):
        # balanced graph
        # strongly connected
        
        return 0
    

if __name__ == "__main__":
    test_matrix = [[0, 0, 0, 1, 0, 0 ,0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0 ,0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0 ,1, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0 ,0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0 ,0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0 ,0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1 ,0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0 ,0, 0, 0, 1],
                   [0, 0, 0, 0, 0, 0 ,0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0 ,1, 0, 0, 0]]
    
    eulerian_graph = Graph(9)
    eulerian_graph.addEdge(test_matrix)
    print(eulerian_graph.graph)

