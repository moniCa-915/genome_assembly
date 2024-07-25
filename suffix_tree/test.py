class Node:
    def __init__(self):
        self.edge = [None] * 256 # ASCII
        self.suffix_link = None
        self.start = -1
        self.end = [] # List for dynamic end updates
        self.suffix_index = -1

class SuffixTree:
    def __init__(self):
        self.root = Node()
        self.leaves = {}

    def build_suffix_tree(self, text):
        string_list = list(text)
        i = -1
        remainder = 0
        active_node = self.root
        active_edge = -1
        active_length = 0

        while i < len(text) - 1:
            i += 1
            remainder += 1

            for leaf in self.leaves.values():
                leaf.end.append(i)

            char_index = ord(string_list[i])

            if active_node.edge[char_index] is not None:
                if active_length == 0:
                    active_edge = active_node.edge[char_index]
                active_length += 1
            else:
                while remainder > 0:
                    if active_length == 0:
                        new_leaf = Node()
                        new_leaf.start = i
                        new_leaf.end.append(i)
                        new_leaf.suffix_index = i
                        self.leaves[i] = new_leaf
                        active_node.edge[char_index] = new_leaf
                        remainder -= 1
                    else:
                        # Handle the internal node creation and splitting logic here
                        # Ensure correct handling of active point updates and suffix link
                        pass

            # Debug code (consider removing or commenting out for production)
            print("Step:", i, "Remainder:", remainder)
            for index, edge in enumerate(self.root.edge):
                if edge is not None:
                    print(f"{index}: {text[edge.start]}")

if __name__ == "__main__":
    text = "bananasna$"
    suffix_tree = SuffixTree()
    suffix_tree.build_suffix_tree(text)
