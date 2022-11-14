from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) > 0:
            listFinished = False
            i = 0
            while not listFinished:
                if nums[i] == val:
                    del nums[i]
                else:
                    i = i + 1
                if i == len(nums):
                    listFinished = True
        return len(nums)