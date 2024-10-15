import math
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m - 1
        row_idx = 0

        while low <= high:
            mid = low + (high - low) // 2
            if mid == m - 1 or matrix[mid][0] <= target < matrix[mid + 1][0]:
                row_idx = mid
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1

        low = 0
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if matrix[row_idx][mid] == target:
                return True
            elif matrix[row_idx][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
