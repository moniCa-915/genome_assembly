class SuffixArray:
    def __init__(self, concatenated_reads):
        self.text = concatenated_reads
        self.text_length = len(self.text)
        self.suffix_array = self.build_suffix_array()
        self.lcp_array = self.build_lcp_array()
    
    def build_suffix_array(self):
        suffixes = sorted((self.text[i:], i) for i in range(self.text_length))
        # print(suffixes)
        return [suffix[1] for suffix in suffixes]
    
    def build_lcp_array(self):
        rank = [0] * self.text_length
        lcp = [0] * (self.text_length - 1)

        for i, suffix in enumerate(self.suffix_array):
            rank[suffix] = i
        
        # height of LCP
        h = 0

        for i in range(self.text_length):
            if rank[i] > 0: # if i is not the first suffix
                j = self.suffix_array[rank[i] - 1] # get the previous suffix in the suffix array
                 # calculate the LCP length between suffix starting at i and at j
                while i + h < self.text_length and j + h < self.text_length and self.text[i + h] == self.text[j + h]:
                    h += 1
                lcp[rank[i] - 1] = h # store LCP length

                if h > 0:
                    h -= 1 # decrease h for the next suffix
        return lcp
    


if __name__ == "__main__":
    reads = ["AGCT", "CTGA", "TGAC", "GACT"]
    concatenated = "$".join(reads) + "$"
    # concatenated = AGCT$CTGA$TGAC$GACT$
    read_boundaries = []
    current_index = 0
    for read in reads:
        read_boundaries.append((current_index, current_index + len(read)))
        current_index += len(read) + 1
    # read_boundaries = [(0, 4), (5, 9), (10, 14), (15, 19)]
    sa = SuffixArray(concatenated)
    # sa.suffix_array = [19, 4, 14, 9, 8, 12, 16, 0, 13, 17, 2, 5, 7, 11, 15, 1, 18, 3, 6, 10]
    print(sa.lcp_array)

