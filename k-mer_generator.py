# Coding problem 3.2.1
# Input: An integer k and a string Text.

# Output: Compositionk(Text), where the k-mers are arranged in lexicographic order.

def mer_generator(string, k):
    length = len(string)
    k_mer = []
    for i in range(0, length - k + 1):
        k_mer.append(string[i: i + k])
    return sorted(k_mer)

if __name__ == "__main__":
    seqence = "TATGGGGTGC"
    print(mer_generator(seqence, 3))
