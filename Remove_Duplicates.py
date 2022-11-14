from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) > 1:
            listFinished = False
            i = 0
            while not listFinished:
                if nums[i] == nums[i+1]:
                    del nums[i+1]
                else:
                    i = i + 1
                if i == len(nums) - 1:
                    listFinished = True
        return len(nums)