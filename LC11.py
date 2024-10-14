from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        result = 0
        l = 0
        r =  len(height) - 1
        while l < r:
            current_height = (r - l) * min(height[l], height[r])
            result = max(current_height, result)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return result