from typing import List
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        h = sorted(nums1 + nums2)
        m = len(h) / 2
        if len(h) % 2 != 0:
            return h[math.floor(m)]
        else:
            return (h[math.floor(m)] + h[math.floor(m) - 1]) / 2
