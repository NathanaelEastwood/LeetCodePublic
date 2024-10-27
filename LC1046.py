import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i, stone in enumerate(stones):
            stones[i] = -stone

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_x = heapq.heappop(stones)
            stone_y = heapq.heappop(stones)
            if stone_y != stone_x:
                heapq.heappush(stones, stone_x - stone_y)


        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0