nucleotides = ["A", "C", "G", "T"]

class Node: # chain_val, and interval (string ID range)
    def __init__(self, chain_val = -1, interval = []):
        self.chain_val = chain_val
        self.interval = interval
        self.children = [None] * 4

class PrefixTree:
    def __init__(self):
        self.root = Node()
    def add_string(self, string_id, string):
        active_node = self.root

        if string_id == 0:         # The first string S 1 can be inserted in one step in a node.
            self.add_first_string(string_id, string)
        else: # not first string
            add_string(active_node, string_id, string)

            
    def add_first_string(self, string_id, string):
        new_node = Node(len(string) - 1, [string_id, string_id])
        first_char = string[0]
        first_char_code = nucleotides.index(first_char)
        self.root.children[first_char_code] = new_node

        #debug code
        print("first string added")
        print("first string start with: " + first_char)
    
    def add_string(self, active_node, string_id, string):
        for char in string:
            char_code = nucleotides.index(char)
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

    test_strings = ["AAGGG", "ACTTT", "AGGCT", "GCCAC", "TCCGC"]
    # initiate Tree
    prefix_tree = PrefixTree()
    # Nodes are added to the tree as the strings S 1 through S k are scanned in order.
    for string_id, string in enumerate(test_strings):
        prefix_tree.add_string(string_id, string)


