import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        rolling_sum = 0

