class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        sorted_map = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        result = []
        for i, j in list(sorted_map.items())[:k]:
            result.append(i)
        return result