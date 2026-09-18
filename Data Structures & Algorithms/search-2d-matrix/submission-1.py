class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_left = 0
        outer_right = len(matrix) - 1

        while outer_left <= outer_right:
            outer_mid = (outer_left + outer_right) // 2

            if matrix[outer_mid][0] <= target and matrix[outer_mid][-1] >= target:
                inner_left = 0
                inner_right = len(matrix[outer_mid]) - 1

                while inner_left <= inner_right:
                    inner_mid = (inner_left + inner_right) // 2

                    if matrix[outer_mid][inner_mid] == target:
                        return True
                    elif matrix[outer_mid][inner_mid] > target:
                        inner_right = inner_mid - 1 
                    else:
                        inner_left = inner_mid + 1
                return False 
            elif matrix[outer_mid][0] > target:
                outer_right = outer_mid - 1
            else:
                outer_left = outer_mid + 1

        return False