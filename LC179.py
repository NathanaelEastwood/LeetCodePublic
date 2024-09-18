from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(num1, num2):
            return int(num2 + num1) - int(num1 + num2)

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(nums)))

