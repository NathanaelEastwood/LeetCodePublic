from copy import copy
from typing import List


class Solution:
    def __init__(self):
        self.result = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.generatePermutations(nums, [])
        return self.result

    def generatePermutations(self, nums, current_list):
        for i, num in enumerate(nums):
            new_current_list = copy(current_list)
            new_current_list.append(num)
            if len(nums) == 1:
                self.result.append(new_current_list)
            else:
                new_nums = copy(nums)
                new_nums.pop(i)
                self.generatePermutations(new_nums, new_current_list)