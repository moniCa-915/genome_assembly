# simulate growth of leaf only
class Node:
    def __init__(self):
        self.edge = [None] * 256 # ASCII
        # suffix link
        self.suffix_link = None
        # start index of the substring (represent edge (start) leading to this node)
        self.start = -1
        # end index of the substring (represent edge (start) leading to this node)
        self.end  = [] # list to faciliate updates
        # index of the suffix (leaf has non-negative value)
        self.suffix_index = -1

class SuffixTree:
    def __init__(self):
        self.root = Node()
        self.leaves = {}


    def build_suffix_tree(self, text):
        # convert text into string list
        string_list = list(text)
        
        # initiate step counter, also serve as index of text
        i = -1

        # remainder
        remainder = 0

        # active point
        active_node = self.root
        active_edge = -1
        active_length = 0

        # create suffix_tree with root
        while i < len(text) - 1:
            i += 1
            remainder += 1
            # update end index of each leaf
            for leaf in self.leaves:
                node = self.leaves[leaf]
                node.end.append(i)

            char_index = ord(string_list[i]) - ord(' ')
            if active_node.edge[char_index] == None:
                while remainder > 0:
                    if active_length == 0:
                        # create new leaf
                        new_leaf = Node()
                        new_leaf.start = i
                        new_leaf.end.append(i)
                        new_leaf.suffix_index = i
                        # link to active_node
                        self.leaves[i] = new_leaf
                        active_node.edge[char_index] = new_leaf
                        remainder -= 1
        
        # debug code
        for edge in self.root.edge:
            if edge is not None:
                print(text[edge.start: edge.end[-1] + 1])

if __name__ == "__main__":
    leaf_text = "abn$"
    suffix_tree = SuffixTree()
    suffix_tree.build_suffix_tree(leaf_text)


