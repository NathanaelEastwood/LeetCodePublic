from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = 0
        prefix_array = []

        for i in range(len(nums)):
            total += nums[i]
            prefix_array.append(nums[i] % p)

        remainder = total % p

        if remainder == 0:
            return 0

        current_best = len(nums)
        for j in range(len(nums)):
            pointer_distance = len(nums) - j
            for k in range(pointer_distance + 1):
                if k > current_best:
                    break
                current_sum = 0
                for l in range(k):
                    current_sum += prefix_array[j+l]
                if current_sum % p == remainder and k < current_best:
                    current_best = k

        if current_best == len(nums):
            return -1
        else:
            return current_best