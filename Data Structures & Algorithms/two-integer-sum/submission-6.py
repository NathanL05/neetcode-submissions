class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_values = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in prev_values:
                return [prev_values.get(difference), i]
            prev_values[nums[i]] = i
        return []