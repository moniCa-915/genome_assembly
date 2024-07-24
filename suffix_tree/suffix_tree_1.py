class Node:
    def __init__(self):
        self.children = [None] * 256 # ASCII
        # suffix link
        self.suffix_link = None
        # start index of the substring (represent edge (start) leading to this node)
        self.start = 0
        # end index of the substring (represent edge (start) leading to this node)
        self.end  = [-1] # list to faciliate updates
        # index of the suffix (leaf has non-negative value)
        self.suffix_index = -1

class SuffixTree:
    def __init__(self):
        self.root = Node()

    # function to create new node
    def create_node(self, start, end): # start: start index of substring, end: end index of substring
        node = Node()
        node.suffix_link = self.root
        node.start = start
        node.end = end
        return node
    
    # get the edge length
    def edge_length(self, node):
        return node.end[0] - node.start + 1
    
    def extend_suffix_tree(self, index_of_char, remainder, active_node, active_edge, active_length):
        leaf_end = index_of_char
        remainder += 1

        while remainder > 0:
            # set up active edge
            
            
            if not active_node.children[active_edge]:
                new_node = self.create_node(index_of_char, [leaf_end])
                active_node.children[active_edge] = new_node
                remainder -= 1
                break

        #debug code


        ###

        
        return 0

    def build_suffix_tree(self, text):
        
        
        

        # remainder
        remainder = 0

        # active point
        active_node = self.root
        active_edge = -1
        active_length = 0

        for i in range(len(text)):
            self.extend_suffix_tree(i, remainder, active_node, active_edge, active_length)




if __name__ == "__main__":
    text = "bananasna$"
    debug_text = "a$"
    suffix_tree = SuffixTree()
    suffix_tree.build_suffix_tree(debug_text)