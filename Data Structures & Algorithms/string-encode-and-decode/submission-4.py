class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "#"
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i])) + delimiter + strs[i]
        return res

    #5#hello
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            res.append(s[j + 1: j + 1 + word_length])
            i = 1 + j + word_length
        return res
