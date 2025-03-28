import heapq
import sys
from heapq import heapify, heappush, nlargest
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)