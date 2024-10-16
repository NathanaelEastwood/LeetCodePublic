from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = l + (r - l) // 2
        # search for a point where the value goes from higher to lower, your result will lie on the right of that point
        # edge case, first value is the smallest
        # edge case, last value is the smallest

        while l < r:
            #e.g. nums = [2, 3, 4, 1], nums[m] = 3 so we are on the left hand side of the list
            if nums[l] > nums[r] and r-l == 1:
                return nums[r]
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m
            m = l + (r - l) // 2

        if nums[m] > nums[0]:
            return nums[0]

        return nums[m]