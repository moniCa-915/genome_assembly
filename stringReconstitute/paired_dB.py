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
    # 1. initiate final_path
    final_path = []
    # 2. get adjacent list
    adjacent_list = paired_dB_graph.adjacent_list
    end_vertex = None
    for key in adjacent_list.keys():
        if not adjacent_list[key]:
            end_vertex = key
    adjacent_list.pop(end_vertex, None)

    # 3. get start node
    start_node = None
    for node in paired_dB_graph.adjacent_list.keys():
        if paired_dB_graph.nodes[node].OUT > 0 and paired_dB_graph.nodes[node].IN == 0:
            start_node = node
            break
    if start_node is None:
        return None

    # 4. append start_node to final path
    final_path.append(start_node)

    # Enter loop to find the trail (contig)
    while True:
        # while_loop_1. initiate trail list to record passed nodes
        trail = []
        # while_loop_2. initiate current_node with start_node
        current = start_node
        # Enter inner while loop (depth first search)
        while True:
            # inner_loop_1. (break point) check if current_node in adjacent_list
            if current not in adjacent_list:
                break
            # inner_loop_2. find the next node linked to current_node, pop it and store it as next_node
            next_node = adjacent_list[current].pop()
            # inner_loop_3. check if current_node has other linked nodes, if not, delete it from adjacent list
            if not adjacent_list[current]:
                adjacent_list.pop(current, None)
            # inner_loop_4. record next_node: append next_node into trail
            trail.append(next_node)
            # inner_loop_5. (break point)check if next_node equal to start_node, if so, that's a loop, break inner while loop
            if next_node == start_node:
                break
            # inner_loop_6. re-define current_node with next_node, repeat
            current = next_node

        # while_loop_3. get the start_index of start in final_path list
        start_index = final_path.index(start_node)
        # while_loop_4. update final_path, combine the following components
            # a. final_path[0: start_index + 1]
            # b. trail
            # c. final_path[start_index + 1:]
        final_path = final_path[0: start_index + 1] + trail + final_path[start_index + 1:]
        # while_loop_5. (break point)if nothing left in adjacent_list: break, else go to step 6
        if not adjacent_list:
            break
        # while_loop_6. initate boolean found_new_start = False
        found_new_start = False
        # while_loop_7. for loop 
            # go thru each vertex in final_path, 
            # (break for loop) if find a vertex in adjacent_list, define start_node with this vertex, and change found_new_start as True
            # (end): if nothing is found
        for vertex in final_path:
            if vertex in adjacent_list:
                start_node = vertex
                found_new_start = True
                break
        # while_loop_8. (break point) if no found_new_start, else start while loop with updated start_node
        if not found_new_start:
            break
    return final_path
    #!! old code
    # conduct depth first search
    # visited = {key: False for key in paired_dB_graph.adjacent_list.keys()}
    # path = [start_node]
    # DFSUtil(start_node, paired_dB_graph.adjacent_list, visited, path)

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
    # text = "TAATGCCATGGGATGTT"
    # k = 3
    # d = 1
    # paired_reads_ = paired_reads(text, k, d)
    # paired_dB_graph = construct_paired_dB(paired_reads_)

    # path = construct_string_from(paired_dB_graph)
    # spelt_text = spell_from_path(path, k, d)

    # print(spelt_text)
    # check_ans(spelt_text, text)

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
    paired_reads_input = []
    with open("paired_reads", "r") as file:
        for line in file.readlines():
            start, end = line.strip().split("|")
            paired_reads_input.append((start, end))

    paired_dB_graph_input = construct_paired_dB(paired_reads_input)

    path = construct_string_from(paired_dB_graph_input)
    seq = spell_from_path(path, k = 50, d = 200)

    with open("paired_reads_ans", "r") as ans_f:
        ans = ans_f.readline().strip()
        check_ans(seq, ans)

    




    

