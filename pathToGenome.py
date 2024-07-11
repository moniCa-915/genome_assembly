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

def pathToGenome(adjacent_list):
    # doing depth-first search (DFS)
    return 0

if __name__ == "__main__":
    patterns = ["AAT", "ATG", "ATG", "ATG", "CAT", "CCA", "GAT", "GCC", "GGA", "GGG", "GTT", "TAA", "TGC", "TGG", "TGT"]
    graph_matrix = overlapGraph(patterns)
    adjacent_list = listGraph(graph_matrix)
    print(adjacent_list)



