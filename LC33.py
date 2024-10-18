from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = l + (r - l) // 2

        # can we do binary search using negative indices? no because we don't know how far we need to wrap around.
        # but we can find the pivot with binary search -  and then binary search between the negative index and the positive

        while l < r:
            #e.g. nums = [2, 3, 4, 1], nums[m] = 3 so we are on the left hand side of the list
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
            m = l + (r - l) // 2

        if nums[0] < nums[len(nums) - 1]:
            m = 0

        # suppose we have [6, 7, 1, 2] m == 2. We want to search between nums[-m] and nums[m]
        l =  -(len(nums) - m)
        r = m - 1
        m = l + (r - l) // 2

        while l <= r:
            if nums[m] == target:
                if m < 0:
                    return len(nums) + m
                else:
                    return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

            m = l + (r - l) // 2

        return -1