def find_most_overlapping(candidate, winner): # (next_index, starting_points[next_index])
    if candidate[1] < winner[1]:
        return candidate
    return winner


if __name__ == "__main__":
    pairs = [[1], [2, 3], [0], [4], [2, 3]]
    starting_points = [1, 2, 1, 2, 2]
    known_value = (None, float('inf'))
    for next_index in pairs[1]:
        known_value = find_most_overlapping((next_index, starting_points[next_index]), known_value)
    print(known_value)
        