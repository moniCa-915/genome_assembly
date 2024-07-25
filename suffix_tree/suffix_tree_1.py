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

            # condition: if string_list[i] == next char after active point
            if active_node.edge[char_index] != None:
                if active_length == 0:
                    active_edge = active_node.edge[char_index]
                active_length += 1
            
            # condition: string_list[i] is not char after active_point -> add leaf or create internal_node
            else:
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
                    else: # active_length != 0 -> create internal_node
                        # debug code
                        print("processing at " + str(i - active_length))
                        print("active_edge is " + text[active_edge.start])
                        print("active_length: " + str(active_length))
                        print("active_node edge: ")
                        for index, edge in enumerate(self.root.edge):
                            if edge is not None:
                                print(str(index) + ": " +text[edge.start])

                        existing_leaf = active_edge

                        internal_node = Node()
                        internal_node.start = existing_leaf.start
                        internal_node.end.append(i - active_length)
                        # create new_leaf
                        new_leaf = Node()
                        new_leaf.start = i
                        new_leaf.end.append(i)
                        new_leaf.suffix_index = i - active_length
                        new_leaf_char_index = ord(text[new_leaf.start]) - ord(" ")
                        # update start of existing leaf
                        existing_leaf.start = internal_node.end[-1] + 1
                        # link existing leaf and new_leaf to internal node
                        existing_leaf_char_index = ord(text[existing_leaf.start]) - ord(" ")
                        internal_node.edge[existing_leaf_char_index] = existing_leaf
                        internal_node.edge[new_leaf_char_index] = new_leaf
                        # replace exisiting leaf with internal node at active_node.edge
                        active_node.edge[existing_leaf_char_index] = internal_node

                        # update remainder and active node
                        remainder -= 1
                        # active_node = no change
                        active_length -= 1

                        print("active node")
                        for index, edge in enumerate(active_node.edge):
                            if edge is not None:
                                print(index)
                        print("before change: " + str(active_edge.suffix_index))
                        active_edge_char_index = ord(text[i - active_length]) - ord(" ")
                        active_edge = active_node.edge[active_edge_char_index]



        
            # debug code
            print("step: " + str(i))
            print("remainder: " + str(remainder))
            for index, edge in enumerate(self.root.edge):
                if edge is not None:
                    print(str(index) + ": " + text[edge.start])
                


if __name__ == "__main__":
    text = "bananasna$"
    building_text = "bananas"
    suffix_tree = SuffixTree()
    suffix_tree.build_suffix_tree(building_text)
