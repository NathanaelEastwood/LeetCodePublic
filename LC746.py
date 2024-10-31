from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # let's construct an array that works backwards from the top of the stair case which is the minimum value to climb from i (i starting at the top)
        cost.reverse()
        costs_array = [0]
        for i, stair in enumerate(cost):
            # remember that we are starting at the top
            if i >= 1:
                costs_array.append(stair + min(costs_array[i], costs_array[i - 1]))
            else:
                costs_array.append(stair)

        return min(costs_array[-1], costs_array[-2])