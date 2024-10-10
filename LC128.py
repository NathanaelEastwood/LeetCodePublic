from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = defaultdict(int)
        result = 0

        for num in nums:
            hash_set[num] = 1

        for num in nums:
            current_length = 0
            if hash_set.get(num-1) is None:
                while hash_set.get(num+current_length) is not None:
                    current_length += 1

            if current_length > result:
                result = current_length

        return result
