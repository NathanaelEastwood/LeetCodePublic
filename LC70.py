class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 -> 1 (total 1)
        # 2 -> 1, 1 or 1, 2 (total 2)
        # 3 -> 1, 1, 1 or 1, 2 or 2, 1 (total 3)
        # 4 -> 1, 1, 1, 1 or 1, 2, 1, or 1, 1, 2 or 2, 1, 1 or 2, 2 (total 5)
        # 5 -> 1, 1, 1, 1, 1 or 1, 2, 1, 1 or 1, 2, 2, or 2, 1, 2 or 2, 2, 1 or 2, 1, 1, 1, or 1, 1, 2, 1 or 1, 1, 1, 2 (total 8)
        # i.e. the answer is just fibonacci(n)
        result = 0
        prev1 = 0
        prev2 = 1
        for i in range(n):
            result = prev1 + prev2
            prev1 = prev2
            prev2 = result

        return result



