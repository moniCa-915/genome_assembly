

class SuffixArray:
    def __init__(self, text):
        self.order = self.buildSuffixArray(text)
        self.len_text = len(text)
        self.text = text

    def sorting(self):
        order = [0] * self.len_text
        count = dict()

        for i in range(self.len_text):
            count[self.text[i]] = count.get(self.text[i], 0) + 1


    def buildSuffixArray(self, text):
        len_text = len(text)
        order = self.sorting(text)


if __name__ == "__main__":
    reads = ["AAC", "GAA", "GTT", "TCG"]

    text = reads[0]
    suffixArrayText = SuffixArray(text)
