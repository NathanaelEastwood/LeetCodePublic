from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i

        for j in range(len(nums)):
            if num_map.get(target - nums[j]) is not None and num_map[target - nums[j]] != j:
                return [j, num_map[target - nums[j]]]