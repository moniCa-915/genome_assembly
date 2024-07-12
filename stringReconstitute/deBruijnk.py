# input: text
# output: adjacent matrix

# define node
class Node:
    def __init__(self, content):
        self.content = content

# build graph
class Graph:
    def __init__(self, text):
        self.text = text


# decide how many mer (k), assume k = 3


def deBruijnk(text, k): # k= k-mer
    # break down the text into fragments, each fragment contain k character, step = 1
    # Figure: 3.4.1
    substrings = [text[i: i + k] for i in range(len(text) - k + 1)]
    # Figure: 3.4.2
    prefix_nodes = [substrings[i][:k-1] for i in range(len(substrings))]
    prefix_nodes.append(substrings[-1][1:])

    general_nodes = sorted(set(prefix_nodes))

    graph = {node: [] for node in general_nodes}
    # add edge
    for i in range(len(prefix_nodes) - 1):
        graph[prefix_nodes[i]].append(prefix_nodes[i + 1])
    print(graph)

if __name__ == "__main__":
    text_1 = "TAATGCCATGGGATGTT"
    text_2 = "AAGATTCTCTAC"
    for k in range(2, 5):
        deBruijnk(text_1, k)

