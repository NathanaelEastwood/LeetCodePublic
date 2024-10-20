from collections import defaultdict
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        result = [max(nums[:k])]
        num_map = defaultdict(int)
        for i in range(k):
            num_map[nums[i]] += 1

        current_max = max(num_map.keys())

        for r in range(k, len(nums)):
            current_max = max(current_max, nums[r])
            num_map[nums[r]] += 1
            num_map[nums[l]] -= 1
            if num_map[nums[l]] == 0:
                num_map.pop(nums[l])
            if nums[l] == current_max:
                current_max = max(num_map.keys())
            result.append(current_max)
            l += 1

        return result