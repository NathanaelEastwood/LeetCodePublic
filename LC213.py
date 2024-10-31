from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        result = max(nums)
        if len(nums) >= 2:
            cumulative_sum = [nums[0], nums[1]]
            for house_number in range(2, len(nums) - 1):
                new_cumulative_sum = max(cumulative_sum[:house_number - 1]) + nums[house_number]
                cumulative_sum.append(new_cumulative_sum)
                result = max(result, new_cumulative_sum)
            print(cumulative_sum)

        return result