from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        gap = 1560
        for i in range(len(timePoints)):
            timePoints[i] = int(timePoints[i][0:2]) * 60 + int(timePoints[i][3:])
        timePoints.sort()

        for j in range(len(timePoints)):
            if abs(timePoints[j] - timePoints[(j + 1) % len(timePoints)]) < gap:
                gap = abs(timePoints[j] - timePoints[(j + 1) % len(timePoints)])
            elif j == len(timePoints) - 1  and abs((timePoints[j] - 1440) - timePoints[(j + 1) % len(timePoints)]) < gap:
                gap = abs((timePoints[j] - 1440) - timePoints[(j + 1) % len(timePoints)])

        return gap
