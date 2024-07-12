def overlapGraph(patterns):
    # Brute force method
    # if suffix of pattern match to prefix of pattern': connect pattern to pattern'
    # transform to adjacent matrix
    adjacent_matrix = [[0 for _ in range(len(patterns))] for _ in range(len(patterns))]
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i != j and patterns[i][1:] == patterns[j][:2]:
                adjacent_matrix[i][j] = 1
    return adjacent_matrix

def listGraph(adjacent_matrix):
    adjacent_graph = {}
    for i in range(len(adjacent_matrix)):
        adjacent_graph[i] = []
        for j in range(len(adjacent_matrix[i])):
            if adjacent_matrix[i][j] == 1:
                adjacent_graph[i].append(j)
    return adjacent_graph

def DFSUtil(node, adjacent_list, visited, patterns, sequence):
    visited[node] = True
    print(adjacent_list[node])
    if adjacent_list[node]:
        for neighbor in adjacent_list[node]:
            if visited[neighbor] == False:
                print("linked to: " + str(neighbor))
                sequence.append(patterns[neighbor][2])
                DFSUtil(neighbor, adjacent_list, visited, patterns, sequence)
    else:
        return visited
    return visited

def pathToGenome(adjacent_list, patterns):
    seqExist = False
    # doing depth-first search (DFS)
    for node in adjacent_list:
        print("start from: " + str(node))
        visited = [False] * len(adjacent_list)
        if not adjacent_list[node]:
            pass
        sequence = [patterns[node]]
        DFSUtil(node, adjacent_list, visited, patterns, sequence)
        
    
        if all(visited) == True:
            print("".join(sequence))
            # seqExist = True
            # return seqExist
    return seqExist

if __name__ == "__main__":
    patterns = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    graph_matrix = overlapGraph(patterns)
    print(graph_matrix)
    adjacent_list = listGraph(graph_matrix)
    print(adjacent_list)
    print(pathToGenome(adjacent_list, patterns))
    # TAATGCCATGGGATGTT
    # TAATGCCATGGATGTTG



