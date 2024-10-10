from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_map = {}
        bucket_sorted = [[] for i in range(len(nums) - 1)]
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        print(count_map)

        for i, c in count_map.items():
            bucket_sorted[c].append(i)

        result = []

        while len(result) < k:
        print(bucket_sorted)
