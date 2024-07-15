def overlapGraph(patterns):
    # Create the adjacency matrix for the overlap graph
    n = len(patterns)
    adjacency_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and patterns[i][1:] == patterns[j][:2]:
                adjacency_matrix[i][j] = 1
    return adjacency_matrix

def listGraph(adjacency_matrix):
    # Convert the adjacency matrix to an adjacency list
    adjacency_list = {}
    for i in range(len(adjacency_matrix)):
        adjacency_list[i] = []
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                adjacency_list[i].append(j)
    return adjacency_list

def DFSUtil(node, adjacency_list, visited, patterns, sequence):
    # Perform a Depth-First Search (DFS) starting from the node
    visited[node] = True
    for neighbor in adjacency_list[node]:
        if not visited[neighbor]:
            sequence.append(patterns[neighbor][-1])  # Append the last character of the next pattern
            DFSUtil(neighbor, adjacency_list, visited, patterns, sequence)

def pathToGenome(adjacency_list, patterns):
    # Perform DFS to find a path that covers all nodes
    for node in adjacency_list:
        visited = [False] * len(adjacency_list)
        sequence = [patterns[node]]  # Start sequence with the current pattern
        DFSUtil(node, adjacency_list, visited, patterns, sequence)
        if all(visited):
            return "".join(sequence)
    return None

if __name__ == "__main__":
    patterns = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    graph_matrix = overlapGraph(patterns)
    print("Adjacency Matrix:")
    for row in graph_matrix:
        print(row)
    adjacent_list = listGraph(graph_matrix)
    print("\nAdjacency List:")
    for key, value in adjacent_list.items():
        print(f"{key}: {value}")
    genome_path = pathToGenome(adjacent_list, patterns)
    print("\nReconstructed Genome Sequence:")
    print(genome_path)


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