#88 - 98

                        # update start of existing leaf or internal_nodes
                        existing_node = Node()
                        existing_node.start = internal_node.end[-1] + 1

                        existing_node.end.append(i) # leaf, internal_node: no change
                        existing_node.suffix_index = active_edge.suffix_index # internal_node: set to -1
                        existing_node_char_index = ord(text[existing_node.suffix_index]) - ord(" ") # internal_node: ord(text[existing_node.start) - ord(" ") 
                        # link existing leaf and new_leaf to internal node
                        internal_node.edge[existing_node_char_index] = existing_node
                        internal_node.edge[new_leaf_char_index] = new_leaf # no new leaf
                        # replace exisiting leaf with internal node at active_node.edge
                        active_node.edge[existing_node_char_index] = internal_node