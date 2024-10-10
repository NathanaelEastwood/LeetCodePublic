from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_right = []
        current_max = nums[-1]
        for i in range(len(nums)):
            if nums[-i - 1] > current_max:
                current_max = nums[-i - 1]
            max_right.append(current_max)

        max_right.reverse()

        result = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > max_right[r]:
                l += 1
            result = max(result, r - l)

        return result
