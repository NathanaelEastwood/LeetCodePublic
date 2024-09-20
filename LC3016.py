from collections import Counter
import math

class Solution:
    def minimumPushes(self, word: str) -> int:
        dict = Counter(list(word))
        frequency = sorted(dict.values(), reverse=True)
        result = 0
        for i in range(len(frequency)):
            result += frequency[i] * math.ceil((i+1)/8)
        return result