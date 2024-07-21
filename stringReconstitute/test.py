def build_reads(text):
    reads = []
    for i in range(len(text) - 5):
        read = text[i: i + 5]
        reads.append(read)
    for i in range(len(text) - 5 + 1, len(text)):
        read = text[i:]
        lack_length = 5 - len(read)
        read += text[:lack_length]
        reads.append(read)
    return reads



if __name__ == "__main__":
    text = "ACGTTCGA"
    print(build_reads(text))