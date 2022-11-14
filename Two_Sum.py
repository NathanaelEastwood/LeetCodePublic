from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 0
        k = 0
        viableNumbers = []
        SolutionFound = False
        NotLooped = False
        # for i in range(len(nums)):
        #    if nums[i] <= target:
        #        viableNumbers.append(nums[i])
        # create a list of viable numbers.
        while not SolutionFound:
            NotLooped = False
            while not SolutionFound and not NotLooped:
                if nums[k] + nums[j] == target and not j == k:
                    SolutionFound = True
                    # print(nums.index(viableNumbers[j]), nums.index(viableNumbers[k], nums.index(viableNumbers[j])+1))
                    # return [nums.index(viableNumbers[j]), nums.index(viableNumbers[k], nums.index(viableNumbers[j])+1)]
                    return [j, k]
                k += 1
                if k == len(nums):
                    NotLooped = True
                    k = j
            j += 1
