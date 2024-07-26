nucleotides = ["A", "C", "G", "T"]

class Node: # chain_len, and interval (string ID range)
    def __init__(self, chain_len = -1, interval = []):
        self.chain_len = chain_len
        self.interval = interval
        self.children = [None] * 4

class PrefixTree:
    def __init__(self):
        self.root = Node()
    def add_string(self, string_id, string):
        current_node = self.root

        if string_id == 0:         # The first string S 1 can be inserted in one step in a node.
            self.add_first_string(string_id, string)
        else: # not first string
            self.add_string(current_node, string_id, string)

            
    def add_first_string(self, current_node, string_id, string):
        new_node = Node(len(string) - 1, [string_id, string_id])
        char = string[0]
        char_code = nucleotides.index(char)
        current_node.children[char_code] = new_node

        #debug code
        print("first string added")
        print("first string start with: " + char)
    
    def add_string(self, string_id, string):
        current_node = self.root
        local_position = 0
        path_len = 0 # total length of all edges in the path plus the total length of all chain_len values for all nodes in this path
        for char in string: 
            if current_node.chain_len >= local_position:
                print("work on ")
                
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


