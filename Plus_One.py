from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            # loop in reverse order by subtracting i from the length of digits
            if digits[(len(digits)) - i - 1] == 9:
                digits[(len(digits)) - i - 1] = 0
                if len(digits) - i - 1 == 0:
                    digits.insert(0, 1)
                    i -= 1
            else:
                digits[(len(digits)) - i - 1] += 1
                return digits
        return digits
