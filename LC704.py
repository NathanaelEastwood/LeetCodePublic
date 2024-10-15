import math
from math import ceil
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pointer = len(nums)//2
        offset = 0
        while len(nums) > 1:
            pointer = len(nums)//2
            if nums[pointer] < target:
                nums = nums[pointer:]
                offset += len(nums[:pointer])
            elif nums[pointer] > target:
                nums = nums[:pointer]
            else:
                return pointer + offset

        if nums[0] == target:
            return offset
        else:
            return -1
