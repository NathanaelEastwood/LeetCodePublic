from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0

        #for num in nums:
        #    hash_set[num] = 1

        for num in set_nums:
            current_length = 0
            if (num-1) not in set_nums:
                while (num + current_length) in set_nums:
                    current_length += 1

            result = max(current_length, result)

        return result
