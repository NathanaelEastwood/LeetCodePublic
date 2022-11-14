from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        element = 0
        for element in range(len(nums)):
            if nums[element] == target:
                return element
            if nums[element] > target and element == 0:
                return 0
            if element == len(nums) - 1:
                return len(nums)
            if nums[element] < target < nums[element + 1]:
                return element + 1
