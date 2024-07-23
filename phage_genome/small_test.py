class TreeNode:
    def __init__(self, label=''):
        self.label = label
        self.children = {}
        self.interval = [float('inf'), float('-inf')]
        self.chain_len = len(label)

    def update_interval(self, i):
        self.interval[0] = min(self.interval[0], i)
        self.interval[1] = max(self.interval[1], i)

    def __str__(self):
        return f"Node(label={self.label}, interval={self.interval})"

class Tree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, s, i):
        current_node = self.root
        path_len = 0
        local_position = 0

        while local_position < len(s):
            if local_position < current_node.chain_len:
                # Matching within the current node
                if s[local_position] != current_node.label[local_position]:
                    break
                local_position += 1
            else:
                # Matching across nodes
                next_char = s[local_position]
                if next_char in current_node.children:
                    current_node = current_node.children[next_char]
                    path_len += current_node.chain_len
                    local_position = path_len
                else:
                    break

        # If no match found, insert the rest of the string
        while local_position < len(s):
            new_node = TreeNode(s[local_position:])
            current_node.children[s[local_position]] = new_node
            current_node = new_node
            local_position += current_node.chain_len

        # Update intervals for all nodes in the path
        current_node.update_interval(i)

    def __str__(self):
        def recurse(node, depth=0):
            ret = "\t" * depth + str(node) + "\n"
            for child in node.children.values():
                ret += recurse(child, depth + 1)
            return ret

        return recurse(self.root)

# Example usage:
sorted_strings = ["apple", "app", "apricot", "banana", "band", "bandana"]
tree = Tree()
for i, s in enumerate(sorted_strings):
    tree.insert(s, i+1)

print(tree)
