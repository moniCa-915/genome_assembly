def find_hamiltonian_path(pairs):
    def backtrack(current_vertex, visited, path):
        # If all vertices are visited, return the path
        if all(visited) == True:
            return path
        
        # Try all possible next vertices
        for neighbor in pairs[current_vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                
                result = backtrack(neighbor, visited, path)
                if result:  # If a valid path is found, return it
                    return result
                
                # Backtrack
                visited[neighbor] = False
                path.pop()
        
        return None


    visited = [False] * len(pairs)
    path = [0]
    visited[0] = True
    
    result = backtrack(0, visited, path)
    if result:  # If a path is found starting from this vertex, return it
        return result
    
    return None  # If no Hamiltonian path is found

# Example usage:
graph = {
    0: [1, 3],
    1: [2],
    2: [0],
    3: [2]
}

path = find_hamiltonian_path(graph)
print("Hamiltonian Path:", path if path else "None found")