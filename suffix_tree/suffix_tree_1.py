class Node:
    def __init__(self):
        self.children = {}
        self.index = -1

class SuffixTree:
    def __init__(self, s):
        self.root = Node()
        self.s = s
        self.build_suffix_tree()

    def build_suffix_tree(self):
        for i in range(len(self.s)):
            print("processing sufiix")
            print(self.s[i:], i)
            self._insert_suffix(self.s[i:], i)

    def _insert_suffix(self, suffix, index):
        current = self.root
        i = 0
        while i < len(suffix):
            if suffix[i] in current.children:
                print(suffix + " enter first if")
                child = current.children[suffix[i]]
                edge_label = self.s[child.index:child.index + len(suffix)]
                j = 0 # track char of suffix
                while j < len(edge_label) and i + j < len(suffix) and suffix[i + j] == edge_label[j]:
                    j += 1
                if j == len(edge_label): # reach end of label, child node becomes current node
                    current = child
                    i += j
                else:
                    # Split edge
                    new_node = Node()
                    new_node.children[edge_label[j]] = child
                    new_node.index = child.index + j
                    current.children[suffix[i]] = new_node
                    child.index += j
                    # Add the remaining suffix part
                    new_leaf = Node()
                    new_leaf.index = index
                    new_node.children[suffix[i + j]] = new_leaf
                    return
            else:
                print("enter first else")
                new_leaf = Node()
                new_leaf.index = index
                current.children[suffix[i]] = new_leaf
                return

    def print_tree(self, node=None, indent=""):
        if node is None:
            node = self.root
        for k, v in node.children.items():
            print(f"{indent}{k}: {self.s[v.index:]}")
            self.print_tree(v, indent + "  ")

# Example usage
s = "banana$"
st = SuffixTree(s)
st.print_tree()
