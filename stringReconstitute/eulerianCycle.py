from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.vertices = num_vertices
        self.graph = defaultdict(list)
        self.IN = [0] * num_vertices

    def addEdge(self, start, end):
        self.graph[start].append(end)

    def matrix_toListGraph(self, adjacent_matrix):
        for i in range(len(adjacent_matrix)):
            for j in range(len(adjacent_matrix[i])):
                if adjacent_matrix[i][j] == 1:
                    self.graph[i].append(j)
                    self.IN[i] += 1

    def DFSUtil(self, start_vertex, visited):
        visited[start_vertex] = True
        for neighbor in self.graph[start_vertex]:
            if not visited[neighbor]:
                self.DFSUtil(neighbor, visited)

    def graphTranspose(self):
        transposeGraph = Graph(self.vertices)
        for node in range(self.vertices):
            for child in self.graph[node]:
                transposeGraph.addEdge(child, node)
        return transposeGraph

    def isSCC(self):
        # forward depth first search
        visited = [False] * self.vertices
        start_vertex = -1
        for i in range(self.vertices):
            if self.graph[i]:
                start_vertex = i
                break
        self.DFSUtil(start_vertex, visited)

        if not all(visited) == True:
            return False
        
        # reverse depth first search
        reverseGraph = self.graphTranspose()
        visited = [False] * self.vertices
        reverseGraph.DFSUtil(start_vertex, visited)

        if not all(visited) == True:
            return False
        return True
    
    def isEulerian(self):
        # if SCC
        if self.isSCC() == False:
            return False
        # Each vertex has same amount of IN and OUT of edge (Balanced)
        for vertex in range(self.vertices):
            if len(self.graph[vertex]) != self.IN[vertex]:
                return False
        return True


# def listGraph(adjacent_matrix):
#     adjacent_graph = defaultdict(list)
#     for i in range(len(adjacent_matrix)):
#         for j in range(len(adjacent_matrix[i])):
#             if adjacent_matrix[i][j] == 1:
#                 adjacent_graph[i].append(j)
#     return adjacent_graph

# def DFSUtil(start_vertex, visited, adjacent_list):
#     visited[start_vertex] = True
#     for neighbor in adjacent_list[start_vertex]:
#         if not visited[neighbor]:
#             DFSUtil(neighbor, visited, adjacent_list)

# def isSCC(graphList):
#     visited = [False] * len(graphList)
#     start_vertex = -1
#     for i in range(len(graph_list)):
#         if graph_list[i]:
#             start_vertex = i
#             break
#     DFSUtil(start_vertex, visited, graph_list)

#     if all(visited) == True:
#         return True
#     return False



# def DFSUtil(node, adjacent_list, visited, patterns, sequence):
#     visited[node] = True
#     print(adjacent_list[node])
#     if adjacent_list[node]:
#         for neighbor in adjacent_list[node]:
#             if visited[neighbor] == False:
#                 print("linked to: " + str(neighbor))
#                 sequence.append(patterns[neighbor][2])
#                 DFSUtil(neighbor, adjacent_list, visited, patterns, sequence)
#     else:
#         return visited
#     return visited

# def pathToGenome(adjacent_list, patterns):
#     seqExist = False
#     # doing depth-first search (DFS)
#     for node in adjacent_list:
#         print("start from: " + str(node))
#         visited = [False] * len(adjacent_list)
#         if not adjacent_list[node]:
#             pass
#         sequence = [patterns[node]]
#         DFSUtil(node, adjacent_list, visited, patterns, sequence)
        
    
#         if all(visited) == True:
#             print("".join(sequence))
#             # seqExist = True
#             # return seqExist
#     return seqExist

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
    
    # graph_list = listGraph(test_matrix)
    # print(isSCC(graph_list))

    graphClass = Graph(len(test_matrix))
    graphClass.matrix_toListGraph(test_matrix)
    print(graphClass.graph)
    print(graphClass.isSCC())
    print(graphClass.isEulerian())


