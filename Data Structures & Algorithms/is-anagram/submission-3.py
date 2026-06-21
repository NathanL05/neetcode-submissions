class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 

        frequency = {}

        for c in s:
            frequency[c] = frequency.get(c, 0) + 1
        
        for c in t:
            if c not in frequency or frequency[c] == 0:
                return  False
            frequency[c] -= 1 
        return True