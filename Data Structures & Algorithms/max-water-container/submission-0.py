class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for left in range(len(heights) - 1):
            for right in range(left + 1, len(heights)):
                if heights[left] < heights[right]:
                    maxWater = max(maxWater, heights[left] * (right - left))
                else:
                    maxWater = max(maxWater, heights[right] * (right - left))
        return maxWater