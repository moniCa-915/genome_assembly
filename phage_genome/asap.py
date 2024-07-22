nucleotides = ["A", "T", "C", "G"]

class Node: # chain_val, and interval (string ID range)
    def __init__(self, chain_val = -1, interval = []):
        self.chain_val = chain_val
        self.interval = interval

class PrefixTrie:
    def __init__(self, reads):
        self.root = Node()
    def add_reads(self, read):
        current_node = self.root
        




    

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
    test_string_1 = "AAGGG"
    tree = PrefixTrie()
    tree.add_reads(test_string_1)
    test_strings = ["AAGGG", "ACTTT", "AGGCT", "GCCAC", "TCCGC"]
