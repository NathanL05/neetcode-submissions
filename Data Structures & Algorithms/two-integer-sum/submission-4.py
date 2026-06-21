class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            difference = target - num

            if difference in hash_map:
                return [hash_map.get(difference), index]
            hash_map[num] = index
        return []