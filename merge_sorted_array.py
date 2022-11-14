from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 1
        pos1 = 0
        pos2 = 0
        while i <= (m+n):
            if nums1[pos1] < nums2[pos2] and nums1[pos1] != 0:
                pos1 += 1
            else:
                nums1.insert(pos1, nums2[pos2])
                pos2 += 1
                pos1 += 1
            i += 1
        del nums1[-n:-1]
        del nums1[-1]
