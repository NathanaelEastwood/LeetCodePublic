from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            current_sum = nums[i]
            for j in range(i + 1, len(nums)):
                if current_sum + nums[j] == target:
                    return [i, j]