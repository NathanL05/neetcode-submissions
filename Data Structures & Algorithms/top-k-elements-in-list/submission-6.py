class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1

        for i, j in count.items():
            frequency[j].append(i)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result
                
                continue

        return result