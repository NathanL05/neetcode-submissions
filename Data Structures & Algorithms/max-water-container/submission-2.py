class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights) - 1):
            current_max = 0
            for j in range(i + 1, len(heights)):
                current_max = max(current_max, (j - i) * min(heights[i], heights[j]))

            max_area = max(max_area, current_max)

        return max_area