from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_height = []
        max_right_height = []
        left_max = 0
        right_max = 0
        result = 0

        for l_h in range(len(height)):
            max_left_height.append(left_max)
            left_max = max(left_max, height[l_h])

        for r_h in range(1, len(height) + 1):
            max_right_height.append(right_max)
            right_max = max(right_max, height[-r_h])

        max_right_height.reverse()

        for i in range(len(height)):
            low_side = min(max_right_height[i], max_left_height[i])
            result += max(low_side - height[i], 0)

        return result
