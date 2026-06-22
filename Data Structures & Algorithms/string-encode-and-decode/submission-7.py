class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + '£' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i

            while s[j] != '£':
                j += 1

            word_length = int(s[i:j])
            start_index = j + 1
            end_index = start_index + word_length
            result.append(s[start_index: end_index])
            i = end_index
        return result