class Node:
    def __init__(self, read_start, read_end):
        self.content = read_start + "|" + read_end
        self.IN = 0
        self.OUT = 0

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacent_list = {}
    
    def add_nodes(self, start, end):
        content = start + "|" + end
        if content not in self.nodes:
            self.nodes[content] = Node(start, end)
            self.adjacent_list[content] = []

    def add_edge(self, prefix, suffix):
        if prefix in self.nodes and suffix in self.nodes:
            self.adjacent_list[prefix].append(suffix)
            self.nodes[suffix].IN += 1
            self.nodes[prefix].OUT += 1

def paired_reads(text, k , d): # generate paired composition
    paired_dB = []
    for i in range(len(text) - d - 2 * k + 1):
        first_k_mer = text[i: i + k]
        last_k_mer = text[i + k + d: i + (2 * k) + d]
        paired_dB.append((first_k_mer, last_k_mer))
    return paired_dB

def construct_paired_dB(paired_reads): # construct paired de Bruijn graph
    paired_dB = Graph()

    for paired_read in paired_reads:
        start = paired_read[0]
        start_prefix = start[:-1]
        start_suffix = start[1:]

        end = paired_read[1]
        end_prefix = end[: -1]
        end_suffix = end[1:]

        paired_dB.add_nodes(start_prefix, end_prefix)
        paired_dB.add_nodes(start_suffix, end_suffix)

        prefix_node = start_prefix + "|" + end_prefix
        suffix_node = start_suffix + "|" + end_suffix

        paired_dB.add_edge(prefix_node, suffix_node)

    return paired_dB

def construct_string_from(paired_dB_graph):
    start_node = None

    for node in paired_dB_graph.adjacent_list.keys():
        if paired_dB_graph.nodes[node].OUT > 0 and paired_dB_graph.nodes[node].IN == 0:
            start_node = node
            break
    if start_node is None:
        return None

    # conduct depth first search
    visited = {key: False for key in paired_dB_graph.adjacent_list.keys()}
    path = [start_node]
    DFSUtil(start_node, paired_dB_graph.adjacent_list, visited, path)
    return path

def DFSUtil(start_vertex, adjacnet_list, visited, path):
    visited[start_vertex] = True
    for neighbor in adjacnet_list[start_vertex]:
        yet_visited = None
        if adjacnet_list[neighbor]:
            for node in adjacnet_list[neighbor]:
                if not visited[node]:
                    yet_visited = node
        if not visited[neighbor] or yet_visited is not None:
            DFSUtil(neighbor, adjacnet_list, visited, path)
            path.append(neighbor)

def dfs_interate(start_vertex, adjacent_list, path, visited):
    # initiate stack with start_vertex
    # pop last vertex in the stack as current
    # find the vertices next to current as next
    # if the vertices are not visited, append into stack
    # find the next vertex from start_vertex
    # if next vertex is not visited and 

    # find the longest path
    return 0


def spell_from_path(path, k, d):
    # initiate
    first, end = path[0].split("|")
    path_to_string = [first]
    path_to_string_end = [end]

    for node in path[1:]:
        start, end = node.split("|")
        path_to_string.append(start[-1])
        path_to_string_end.append(end[-1])

    for end in path_to_string_end[-(k + d):]:
        path_to_string.append(end)

    return "".join(path_to_string)
    
def check_ans(result, ans):
    if result == ans:
        print("correct")

if __name__ == "__main__":
    # test code for coding
    text = "TAATGCCATGGGATGTT"
    k = 3
    d = 1
    paired_reads_ = paired_reads(text, k, d)
    paired_dB_graph = construct_paired_dB(paired_reads_)
    print(paired_dB_graph.adjacent_list)
    path = construct_string_from(paired_dB_graph)
    print(path)
    seq = spell_from_path(path, k, d)
    print(seq)
    check_ans(seq, text)

    # Example_1

    # reads_1 = ["GAGA|TTGA", "TCGT|GATG", "CGTG|ATGT", "TGGT|TGAG", "GTGA|TGTT", "GTGG|GTGA", "TGAG|GTTG", "GGTC|GAGA", "GTCG|AGAT"]
    # paired_reads_1 = []
    # for read in reads_1:
    #     start, end = read.split("|")
    #     paired_reads_1.append((start, end))
    # paired_dB_graph_1 = construct_paired_dB(paired_reads_1)
    # path = construct_string_from(paired_dB_graph_1)
    # print(path)
    # seq = spell_from_path(path, k = 4, d = 2)
    # print(seq)
    # ans = "GTGGTCGTGAGATGTTGA"
    #     #   "GTG GTC GTG AGA  GT TGA"
    # check_ans(seq, ans)
    
    # "GTGGTCGTGAGA TGTTGA" "(4 + 2, k + d)"

    # driver code
    # paired_reads_input = []
    # with open("paired_reads", "r") as file:
    #     for line in file.readlines():
    #         start, end = line.strip().split("|")
    #         paired_reads_input.append((start, end))

    # paired_dB_graph_input = construct_paired_dB(paired_reads_input)

    # path = construct_string_from(paired_dB_graph_input)
    # seq = spell_from_path(path, k = 50, d = 200)
    # print(seq)
    




    

