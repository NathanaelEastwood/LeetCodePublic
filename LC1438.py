from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        current_max = 0
        current_high = 0
        current_low = float('inf')
        p2 = 0
        for p1 in range(len(nums) - 1):
            while p2 < len(nums[p1:]):
                p2 += 1
                current_high = current_high if current_high > nums[p2+p1] else nums[p2+p1]
                current_low = current_low if current_low < nums[p2+p1] else nums[p2+p1]
                if current_high - current_low > limit or p2+p1 == len(nums[p1:]):
                    current_max = current_max if current_max > ((p2+p1) - p1) else ((p2+p1) - p1)
                    current_low = float('inf')
                    current_high = 0
            p2 = p1
        return current_max
