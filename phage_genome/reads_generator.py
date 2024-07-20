# based on genome input, generate artificial reads
def generator(genome, reads_len, overlap_len):
    reads = []
    for i in range(0, len(genome) - reads_len + 1, reads_len - overlap_len):
        reads.append(genome[i: i + reads_len])
    return reads

if __name__ == "__main__":
    with open("phiX174.txt", "r") as file:
        sequence = file.read()

    read_length = 100
    overlap_length = 99
    reads = generator(sequence, read_length, overlap_length)
    
    # output reads
    with open("reads.txt", "w") as output:
        for read in reads:
            output.write(read + '\n')
