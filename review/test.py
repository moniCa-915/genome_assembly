def build_suffix_array(text):
    suffixes = [(text[i:], i) for i in range(len(text))]
    sorted_suffixes = sorted(suffixes)
    return [suffix[1] for suffix in sorted_suffixes]

def build_lcp_array(suffix_array):
    rank = [0] * len(suffix_array)
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    print(rank)

if __name__ == "__main__":
    text = "AGCT$"
    suffix_array = build_suffix_array(text)
    build_lcp_array(suffix_array)