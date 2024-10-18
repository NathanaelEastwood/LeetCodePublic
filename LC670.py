import math


class Solution:
    def maximumSwap(self, num: int) -> int:
        positions = math.floor(math.log10(num))
        char_array = []

        for i in range(positions, -1, -1):
            remainder = num // 10 ** i % 10
            char_array.append(remainder)
            i -= 1

        for j in range(0, len(char_array) - 1):
            if char_array[j] < char_array[j+1]:
                left = char_array[j]
                right = char_array[j+1]
                char_array[j] = right
                char_array[j+1] = left
                break

        result = 0
        for k in range(len(char_array), 0, -1):
            result += char_array[-k] * (10 ** (k - 1))

        return result