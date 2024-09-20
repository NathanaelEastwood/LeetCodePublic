from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n+1):
            count = bin(i).count('1')
            result.append(count)
        return result
