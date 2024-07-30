nucleotides = ["A", "C", "G", "T"]

class Node: # chain_len, and interval (string ID range)
    def __init__(self, chain_len = 0, interval = []):
        self.chain_len = chain_len
        self.interval = interval
        self.children = [None] * 4

class PrefixTree:
    def __init__(self, strings):
        self.root = Node()
        self.strings = strings
    def build_suffix_tree(self):

        for string_id, string in enumerate(self.strings):
            current_node = self.root

            path_len = 0 # total length of all edges in the path plus the total length of all chain_len values for all nodes in this path
            if string_id == 0:         # The first string S 1 can be inserted in one step in a node.
                self.add_first_string(current_node, string_id, string, path_len)

            else: # not first string
                self.add_string(string_id, string, path_len)
            
            # debug code
            print(f"finish string [{string_id}]")
            initiate_char = string[0]
            initiate_code = nucleotides.index(initiate_char)
            if self.root.children[initiate_code] != None:
                node = self.root.children[initiate_code]
                print(f"root -> {initiate_char}, {string[1: 1 + node.chain_len]}, interval = {node.interval}")
                for child_node in node.children:
                    if child_node is not None:
                        print(f"\t-> node.interval = {child_node.interval} node.chain_len = {child_node.chain_len}")
                        for child_child_node in child_node.children:
                            if child_child_node is not None:
                                print(f"\t\t-> node.interval = {child_child_node.interval} node.chain_len = {child_child_node.chain_len}")
                print("\n")
        
        #debug code
        print("final suffix tree")
        for layer_1 in self.root.children:
            path = 0
            if layer_1 is not None:
                print(f"start from {self.strings[layer_1.interval[0]][path: path + layer_1.chain_len + 1]}, chain_len = {layer_1.chain_len}, interval = {layer_1.interval}")
                path += (layer_1.chain_len + 1)
                for layer_2 in layer_1.children:
                    if layer_2 is not None:
                        print(f"\t->{self.strings[layer_2.interval[0]][path: path + layer_2.chain_len + 1]}, chain_len = {layer_2.chain_len},  interval = {layer_2.interval}")

    def add_first_string(self, current_node, string_id, string, path_len):
        new_node = Node(len(string) - path_len - 1, [string_id, string_id])
        char = string[path_len]
        char_code = nucleotides.index(char)
        current_node.children[char_code] = new_node

        #debug code
        print("first string added")
        print("first string start with: " + char)
    
    def add_string(self, string_id, string, path_len):

        current_node = self.root
        local_position = 1
        for char in string: 
            char_code = nucleotides.index(char)
            # mismatch: ex. "A 'A' GGG", "A 'C' TTT"
            if current_node.chain_len >= local_position:
                print("work on ")
                compare_char = None
                if path_len < len(string):
                    compare_char = self.strings[current_node.interval[0]][path_len]
                    print(f"char = {char} and compare character = {compare_char}")
                if compare_char == char:
                    local_position += 1
                    path_len += 1
                else:
                    # split into two nodes: v1 and v2, v1 is parent of v2
                    # v1 = Node(local_position - 1, current_node.interval)
                    # if path_len < len(string):
                    #     v1_char_code = nucleotides.index(self.strings[v1.interval[0]][path_len - 1])
                    # else:
                    #     print(f"path_len: {path_len} >= string_length: {len(string)}")
                    #     break
                    v2 = Node(current_node.chain_len - local_position, [current_node.interval[0], current_node.interval[1] - 1])
                    v2_char_code = nucleotides.index(self.strings[v2.interval[0]][path_len]) # should use path_len instead of local_position?
                    current_node.children[v2_char_code] = v2
                    v3 = Node(len(string) - path_len - 1, [string_id, string_id])
                    v3_char_code = nucleotides.index(char)
                    current_node.children[v3_char_code] = v3
                    current_node.chain_len = local_position - 1
                    
                    # debug code
                    for node in self.root.children:
                        if node is not None:
                            print(f"root -> node.interval = {node.interval}, node.chain_len = {node.chain_len}")
                    break
            else: # " 'A'AGGG ", " 'A' CTTT" # match occur
                if current_node.children[char_code] != None:
                    #debug
                    print(f"original current_node chain_len = {current_node.chain_len}, interval = {current_node.interval}")
                    path_len += (current_node.chain_len + 1)
                    current_node.children[char_code].interval[-1] = string_id
                    current_node = current_node.children[char_code]
                    # debug
                    print(f"current_node chain_len = {current_node.chain_len}, current_node.interval = {current_node.interval}")

                else: # new char for current node
                    self.add_first_string(current_node, string_id, string, path_len)
                    break
            # mismatch

    def find_suffix_prefix_pairs(self):
        pairs = [None] * len(self.strings)
        starting_points = [-1] * len(self.strings)
        for string_index, string in enumerate(self.strings):
            starting_point = 1
            print(f"process string_index {string_index}: {string}")
            while starting_point < len(string): # check each suffix of string
                current_node = self.root
                local_position = 1
                path_len = 0
                found, pair = self.find_matched_prefix(starting_point, string, current_node, local_position, path_len)
                if found:
                    pairs[string_index] = pair
                    starting_points[string_index] = starting_point
                    break
                else:
                    starting_point += 1
                     
        return pairs, starting_points

    def find_matched_prefix(self, starting_point, string, current_node, local_position, path_len):
        found = False
        pair = []
        position_of_suffix = starting_point
        print(f"\tprocess suffix: {string[starting_point:]}")
        while position_of_suffix < len(string):
            current_suffix_char = string[position_of_suffix]
            current_suffix_char_index = nucleotides.index(current_suffix_char)
            # case 1: find prefix-suffix match
            if position_of_suffix == len(string) - 1:
                print(f"\t\tenter case 1")
                if len(current_node.interval) > 1 and path_len + local_position - 1 < len(self.strings[current_node.interval[0]]):
                    compare_char = None
                    if current_node.chain_len == 0 and current_node.children[current_suffix_char_index] is not None:
                        current_node = current_node.children[current_suffix_char_index]
                        found = True
                        for index in range(current_node.interval[0], current_node.interval[1] + 1):
                            pair.append(index)
                        return found, pair
                    if current_node.chain_len != 0:
                        compare_char = self.strings[current_node.interval[0]][path_len + local_position - 1]
                        print(f"\t\t{current_suffix_char} compare to {compare_char}")
                        if current_suffix_char == compare_char:
                            print(f"\t\tenter case 1")
                            found = True
                            for index in range(current_node.interval[0], current_node.interval[1] + 1):
                                pair.append(index)
                            return found, pair
                        else:
                            break
                if current_node.chain_len == 0 and current_node.children[current_suffix_char_index] is not None:
                    current_node = current_node.children[current_suffix_char_index]
                    found = True
                    for index in range(current_node.interval[0], current_node.interval[1] + 1):
                        pair.append(index)
                    return found, pair
                else: break
            # case 2: within same node
            if local_position <= current_node.chain_len:
                if path_len + local_position - 1 < len(self.strings[current_node.interval[0]]):
                    print(f"enter case 2")
                    compare_char = self.strings[current_node.interval[0]][path_len + local_position - 1]
                    if current_suffix_char == compare_char:
                        local_position += 1
                        position_of_suffix += 1
                    else:
                        break
                else:
                    break
            # case 3: to next node
            else:
                
                if current_node.children[current_suffix_char_index] != None:
                    print(f"\t\tenter case 3")
                    path_len += (current_node.chain_len + 1)
                    current_node = current_node.children[current_suffix_char_index]
                    position_of_suffix += 1
                else:
                    break
        return found, pair


    def build_seq(self):
        pairs, starting_points = self.find_suffix_prefix_pairs()
        # build sequence by passing thru each pair from index = 0
        for string_index in range(len(starting_points)):
            visited = [False] * len(starting_points)
        sequence = []

# Once you find all the suffix-prefix pair matches between reads, you don't need to use a graph data structure to reconstruct the entire genome - just start at the first read, greedily merge it with the highest-overlapping read in its' list of overlapping pairs (that hasn't already been used), then mark the starting read as visited, and continue

# Once all the reads had been used in the reconstruction, use a simple "longest suffix-prefix of a single string" algorithm to trim the ends off the final sequence - this removes the loop from the final read to the first read in the circular sequence

    def depth_first_search(self, starting_index, pairs, starting_points, visited):
        visited[starting_index] = True
        while True:
            for next_index in range(pairs[starting_index][0], pairs[starting_index][1]):
                if visited[next_index] == False:
                    self.depth_first_search(next_index, pairs, starting_points)

if __name__ == "__main__":

    test_strings = ["AAGGG", "ACTTG", "ACTTT", "AGGCT", "CTAAA", "GCCAC", "TCCGC", "TGACT"]
    test_strings_2 = ["AAC", "ACG", "GAA", "GTT", "TCG"]

    # initiate Tree
    prefix_tree = PrefixTree(test_strings_2)
    prefix_tree.build_suffix_tree()
    print(prefix_tree.find_suffix_prefix_pairs())


