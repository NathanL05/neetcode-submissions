class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        my_set = set(nums)

        longest = 0

        for n in my_set:
            count = 1
            current = n
            while current + 1 in my_set:
                count += 1
                current += 1

            longest = max(count, longest)
        return longest



