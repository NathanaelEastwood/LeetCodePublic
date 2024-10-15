class Solution:
    def minimumSteps(self, s: str) -> int:
        one_count = 0
        zero_count = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1
            else:
                zero_count += 1
                result += one_count

        return result