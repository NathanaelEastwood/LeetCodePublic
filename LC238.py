from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1]
        suffix_array = []

        # calculate prefixes
        for i in range(len(nums) - 1):
            if i == 0:
                prefix_array.append(nums[i])
            else:
                prefix_array.append(nums[i] * prefix_array[-1])

        # reverse and calculate postfixes
        for i in range(len(nums) - 1):
            if i == 0:
                suffix_array.append(nums[-1])
            else:
                suffix_array.append(nums[-i - 1] * suffix_array[-1])
        suffix_array.reverse()
        suffix_array.append(1)

        result = []
        for i in range(len(nums)):
            result.append(prefix_array[i] * suffix_array[i])

        return result
