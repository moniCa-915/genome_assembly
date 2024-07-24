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

class Edge:
    def __init__(self, start_index, end_index):
        self.start = start_index
        self.end = end_index
        self.From = None
        self.To = None
        self.char = None

class SuffixTree:
    def __init__(self):
        self.root = Node()
        self.leaves = {}


    def build_suffix_tree(self, text):
        # convert text into string list
        string_list = list(text)

        i = -1 # initiate step counter, also serve as index of text
        remainder = 0 # remainder
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
            # condition: add leaf
            if active_node.edge[char_index] == None:
                while remainder > 0:
                    if active_length == 0:
                        # create new leaf
                        new_leaf = Node()
                        new_leaf.start = i
                        new_leaf.end.append(i)
                        new_leaf.suffix_index = i
                        # create new edge
                        new_edge = Edge(new_leaf.start, new_leaf.end[-1])
                        new_edge.From = active_node
                        new_edge.To = new_leaf
                        new_edge.char = string_list[i]
                        # link to active_node
                        self.leaves[i] = new_leaf
                        active_node.edge[char_index] = new_leaf
                        remainder -= 1
                    else: # active_length != 0
                        internal_node = Node()
                        # link existing leaf to internal node
                        existing_leaf = active_edge
                        
                        # create new leaf and link to internal node
                        # replace exisiting leaf with internal node
            # condition: if string_list[i] == next char after active point
            else:
                if active_length == 0:
                    active_edge = active_node.edge[char_index]
                active_length += 1
                print(active_length)
                print(remainder)
                print("active_edge: " + text[active_edge.start])
        
        # debug code
        for edge in self.root.edge:
            if edge is not None:
                print(text[edge.start: edge.end[-1] + 1])


if __name__ == "__main__":
    text = "bananasna$"
    building_text = "banana"
    suffix_tree = SuffixTree()
    suffix_tree.build_suffix_tree(building_text)
