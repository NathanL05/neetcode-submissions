class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        my_set = set(nums)
        longest  = 0

        for n in nums:
            if (n - 1) not in my_set:
                length = 1
                current = n
                while current + 1 in my_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest