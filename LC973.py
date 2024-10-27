import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for point in points:
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            distance_point_tuple = (distance, point)
            heapq.heappush(distances, distance_point_tuple)

        results = heapq.nsmallest(k, distances)
        return_value = []
        for result in results:
            return_value.append(result[1])
        return return_value
