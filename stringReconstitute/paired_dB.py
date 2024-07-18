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
        # self.nodes[content].append(Node(start, end))


    def add_edge(self, prefix, suffix):
        if prefix in self.nodes and suffix in self.nodes:
            self.adjacent_list[prefix].append(suffix)
            self.nodes[suffix].IN += 1
            self.nodes[prefix].OUT += 1
            # print(self.nodes[suffix][0].content)

def paired_reads(text, k , d): # generate paired composition
    paired_dB = []
    for i in range(len(text) - d - 2 * k + 1):
        first_k_mer = text[i: i + k]
        last_k_mer = text[i + k + d: i + (2 * k) + d]
        paired_dB.append((first_k_mer, last_k_mer))
    return paired_dB

def paired_dB(paired_read): # preliminary version for single pair, can be deleted
    paired_bBgraph = Graph()

    start = paired_read[0]
    start_prefix = start[:-1]
    start_suffix = start[1:]

    end = paired_read[1]
    end_prefix = end[: -1]
    end_suffix = end[1:]

    paired_bBgraph.add_nodes(start_prefix, end_prefix)
    paired_bBgraph.add_nodes(start_suffix, end_suffix)

    prefix_node = start_prefix + "|" + end_prefix
    suffix_node = start_suffix + "|" + end_suffix

    paired_bBgraph.add_edge(prefix_node, suffix_node)


    # Print the nodes to verify
    for content, nodes in paired_bBgraph.nodes.items():
        for node in nodes:
            print(node.content)
    print(paired_bBgraph.adjacent_list)

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

    # Print the nodes to verify
    # for content, nodes in paired_dB.nodes.items():
    #     for node in nodes:
    #         print(node.content)
    print("adjacent list: ")
    print(paired_dB.adjacent_list)

    return paired_dB

def construct_string_from(paired_dB_graph):
    start_node = None
    end_node = None
    for node in paired_dB_graph.adjacent_list.keys():
        if paired_dB_graph.nodes[node].IN > 0 and paired_dB_graph.nodes[node].OUT == 0:
            end_node = node
        if paired_dB_graph.nodes[node].OUT > 0 and paired_dB_graph.nodes[node].IN == 0:
            start_node = node

    # conduct depth first search
    visited = {key: False for key in paired_dB_graph.adjacent_list.keys()}
    path = []
    DFSUtil(start_node, paired_dB_graph.adjacent_list, visited, path)
    path.append(start_node)
    path.reverse()

    return path

def DFSUtil(start_vertex, adjacnet_list, visited, path):
    visited[start_vertex] = True
    for neighbor in adjacnet_list[start_vertex]:
        yet_visited = None
        if adjacnet_list[neighbor]:
            for node in adjacnet_list[neighbor]:
                if visited[node] == False:
                    yet_visited = node
        if visited[neighbor] == False or yet_visited != None:
            DFSUtil(neighbor, adjacnet_list, visited, path)
            path.append(neighbor)

def spell_from_path(path, k):
    return 0


if __name__ == "__main__":
    # test code for coding
    text = "TAATGCCATGGGATGTT"
    k = 3
    d = 1
    paired_reads_ = paired_reads(text, k, d)
    paired_dB_graph = construct_paired_dB(paired_reads_)
    path = construct_string_from(paired_dB_graph)
    print(path)

    "TAATGCCATGGGA TGTT"

    # reads_1 = ["GAGA|TTGA", "TCGT|GATG", "CGTG|ATGT", "TGGT|TGAG", "GTGA|TGTT", "GTGG|GTGA", "TGAG|GTTG", "GGTC|GAGA", "GTCG|AGAT"]
    # paired_reads_1 = []
    # for read in reads_1:
    #     start, end = read.split("|")
    #     paired_reads_1.append((start, end))
    # paired_dB_graph_1 = construct_paired_dB(paired_reads_1)
    # construct_string_from(paired_dB_graph_1)
    
    "GTGGTCGTGAGA TGTTGA" "(4 + 2, k + d)"
    



    

