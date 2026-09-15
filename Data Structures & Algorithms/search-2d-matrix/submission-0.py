class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if (matrix[mid][0] <= target) and (matrix[mid][len(matrix[mid]) - 1] >= target):
                matrix_left = 0
                matrix_right = len(matrix[mid]) - 1

                while matrix_left <= matrix_right:
                    matrix_mid = (matrix_left + matrix_right) // 2

                    if matrix[mid][matrix_mid] == target:
                        return True
                    elif matrix[mid][matrix_mid] < target:
                        matrix_left = matrix_mid + 1
                    else:
                        matrix_right = matrix_mid - 1
                return False

            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

