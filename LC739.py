from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []

        for i,t in enumerate(temperatures):
            while temp_stack and temp_stack[-1][0] < t:
                stackT, stackI = temp_stack.pop()
                result[stackI] = i - stackI
            temp_stack.append([t, i])

        return result