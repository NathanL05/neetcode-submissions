class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        answer = high

        while low <= high:
            mid = (low + high) // 2
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i]/mid)

            if total <= h:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer