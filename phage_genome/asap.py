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
                self.add_first_string(current_node, string_id, string)
                path_len += len(string)
            else: # not first string
                self.add_string(string_id, string, path_len)
            
            # debug code
            print(f"finish string [{string_id}]")
            initiate_char = string[0]
            initiate_code = nucleotides.index(initiate_char)
            if self.root.children[initiate_code] != None:
                node = self.root.children[initiate_code]
                print(f"path pass thru {initiate_char}, {string[1: 1 + node.chain_len]}")

            
    def add_first_string(self, current_node, string_id, string):
        new_node = Node(len(string) - 1, [string_id, string_id])
        char = string[0]
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
                if compare_char == char:
                    local_position += 1
                    path_len += 1
                else:
                    # split into two nodes: v1 and v2, v1 is parent of v2
                    v1 = Node(local_position - 1, current_node.interval)
                    v1_char_code = nucleotides.index(self.strings[v1.interval[0]][len(string) - path_len])
                    v2 = Node(current_node.chain_len - local_position, [current_node.interval[0], current_node.interval[1] - 1])
                    v2_char_code = nucleotides.index(self.strings[v2.interval[0]][len(string) - local_position - 1]) # should use path_len instead of local_position?
                    v1.children[v2_char_code] = v2
                    v3 = Node(len(string) - path_len - 1, [string_id, string_id])
                    v3_char_code = nucleotides.index(char)
                    v1.children[v3_char_code] = v3
                    current_node.children[v1_char_code] = v1
                    break
            else: # " 'A'AGGG ", " 'A' CTTT" # match occur
                if current_node.children[char_code] != None:
                    current_node.children[char_code].interval[-1] = string_id
                    current_node = current_node.children[char_code]
                    path_len += (current_node.chain_len + 1)
                else: # new char for current node
                    self.add_first_string(current_node, string_id, string)
                    break
            # mismatch
                
        return 0
    

def compact_prefix_tree(reads):
    for read in reads:
        print(read)
    # id number for each string
    # each string is represented by a path from root to leaf
    # the edge between each node and its parent node has a label (one of A, C, G, T)
    # each node has an interval [r1, .., r2], r1, ..., r2 are id number
    # each node has its own chain_len value
    return 0

if __name__ == "__main__":

    test_strings = ["AAGGG", "ACTTG", "ACTTT"]
                    #, "AGGCT", "GCCAC", "TCCGC"]
    # initiate Tree
    prefix_tree = PrefixTree(test_strings)
    prefix_tree.build_suffix_tree()
    # Nodes are added to the tree as the strings S 1 through S k are scanned in order.
    # for string_id, string in enumerate(test_strings):
    #     prefix_tree.add_string(string_id, string)


