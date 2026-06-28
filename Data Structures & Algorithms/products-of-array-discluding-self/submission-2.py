class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zero_count = 0
        total_product = 1

        for n in nums:
            if n == 0:
                zero_count +=  1
            else:
                total_product *= n

        for n in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if n == 0:
                    result.append(total_product)
                else:
                    result.append(0)

            else:
                result.append(total_product // n)

        return result