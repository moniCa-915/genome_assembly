if __name__ == "__main__":
    strings = ["AAGGG", "ACTTG", "ACTTT", "AGGCT", "GCCAC", "TCCGC"]
    pairs = [None] * len(strings)
    for string_index, string in enumerate(strings):
        starting_point = 1
        print(string)
        while starting_point < len(string):
            if starting_point == len(string) - 1:
                print("found")
                break
        