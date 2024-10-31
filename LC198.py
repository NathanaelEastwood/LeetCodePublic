from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # maybe similar to the climbing stairs problem
        # remove this at the end as the direction the list goes in does not matter, just makes it easier to think about
        if len(nums) >= 2:
            cumulative_sum = [nums[0], nums[1]]
            result = max(cumulative_sum)
            for house_number in range(2, len(nums)):
                new_cumulative_sum = max(cumulative_sum[:house_number - 1]) + nums[house_number]
                cumulative_sum.append(new_cumulative_sum)
                result = max(result, new_cumulative_sum)
        else:
            result = max(nums)

        return result