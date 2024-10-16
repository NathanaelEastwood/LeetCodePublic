import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # define a high of eating the largest pile on one shot
        # define a low of 1 (no edge cases as the smallest problem will be 1 pile of 1)

        low = 1
        high = max(piles)
        mid = low + ((high - low) // 2)
        # now binary search between high and low to try and find the lowest example which works
        while low < high:
            current_time = self.find_time(self, piles.copy(), mid)
            if current_time > h:
                low = mid + 1
            elif current_time <= h:
                high = mid
            mid = low + ((high - low) // 2)
        return mid


    def find_time(self, piles: List[int], eating_speed: int):
        result = 0
        while len(piles) > 0:
            result += math.ceil(piles[-1]/eating_speed)
            piles.pop()

        return result