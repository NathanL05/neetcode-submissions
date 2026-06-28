class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True

        my_array = []

        for c in s:
            if c.isalnum():
                my_array.append(c.lower())

        left = 0
        right = len(my_array) - 1

        while left < right:
            if my_array[left] != my_array[right]:
                return False
            left += 1 
            right -= 1

        return True

