def construct_string_from(paired_dB_graph):
    # 1. initiate final_path
    final_path = []
    # 2. get adjacent list
    adjacent_list = paired_dB_graph.adjacent_list
    end_vertex = None
    for key in adjacent_list.keys():
        if not adjacent_list[key]:
            end_vertex = key
        adjacent_list.pop(end_vertex, None)
    print(adjacent_list)

    # 3. get start node
    start_node = None
    for node in paired_dB_graph.adjacent_list.keys():
        if paired_dB_graph.nodes[node].OUT > 0 and paired_dB_graph.nodes[node].IN == 0:
            start_node = node
            break
    if start_node is None:
        return None

    # 4. append start_node to final path
    final_path.append(start_node)

    # Enter loop to find the trail (contig)
    while True:
        # while_loop_1. initiate trail list to record passed nodes
        trail = []
        # while_loop_2. initiate current_node with start_node
        current = start_node
        # Enter inner while loop (depth first search)
        while True:
            # inner_loop_1. (break point) check if current_node in adjacent_list
            if current not in adjacent_list:
                break
            # inner_loop_2. find the next node linked to current_node, pop it and store it as next_node
            next_node = adjacent_list[current].pop()
            # inner_loop_3. check if current_node has other linked nodes, if not, delete it from adjacent list
            if not adjacent_list[current]:
                adjacent_list.pop(current, None)
            # inner_loop_4. record next_node: append next_node into trail
            trail.append(next_node)
            # inner_loop_5. (break point)check if next_node equal to start_node, if so, that's a loop, break inner while loop
            if next_node == start_node:
                break
            # inner_loop_6. re-define current_node with next_node, repeat
            current = next_node

        # while_loop_3. get the start_index of start in final_path list
        start_index = final_path.index(start_node)
        # while_loop_4. update final_path, combine the following components
            # a. final_path[0: start_index + 1]
            # b. trail
            # c. final_path[start_index + 1:]
        final_path = final_path[0: start_index + 1] + trail + final_path[start_index + 1:]
        # while_loop_5. (break point)if nothing left in adjacent_list: break, else go to step 6
        if not adjacent_list:
            break
        # while_loop_6. initate boolean found_new_start = False
        found_new_start = False
        # while_loop_7. for loop 
            # go thru each vertex in final_path, 
            # (break for loop) if find a vertex in adjacent_list, define start_node with this vertex, and change found_new_start as True
            # (end): if nothing is found
        for vertex in final_path:
            if vertex in adjacent_list:
                start_node = vertex
                found_new_start = True
                break
        # while_loop_8. (break point) if no found_new_start, else start while loop with updated start_node
        if not found_new_start:
            break
    return final_path