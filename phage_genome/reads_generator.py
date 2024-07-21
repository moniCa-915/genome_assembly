# based on genome input, generate artificial reads
def linear_generator(genome, reads_len, overlap_len):
    reads = []
    for i in range(0, len(genome) - reads_len + 1, reads_len - overlap_len):
        reads.append(genome[i: i + reads_len])
    return reads

def circular_generator(genome, reads_len, overlap_len):
    reads = []
    for i in range(len(genome) - overlap_len):
        read = genome[i: i + reads_len]
        reads.append(read)
    for i in range(len(genome) - overlap_len + 1, len(genome)):
        read = genome[i:]
        lack_length = reads_len - len(read)
        read += genome[:lack_length]
        reads.append(read)
    return reads


if __name__ == "__main__":
    # with open("phiX174.txt", "r") as file:
    #     sequence = file.read()

    # read_length = 100
    # overlap_length = 99
    # reads = linear_generator(sequence, read_length, overlap_length)
    
    # # output reads
    # with open("reads.txt", "w") as output:
    #     for read in reads:
    #         output.write(read + '\n')

    # text = "ACGTTCGA"
    # reads = circular_generator(text, 5, 4)

    with open("phiX174.txt", "r") as file:
        sequence = file.read()

    read_length = 100
    overlap_length = 80
    reads = linear_generator(sequence, read_length, overlap_length)
    
    # output reads
    with open("reads_from_plasmid.txt", "w") as output:
        for read in reads:
            output.write(read + '\n')