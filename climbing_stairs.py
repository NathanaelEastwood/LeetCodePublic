class Solution:
    def climbStairs(self, n: int) -> int:
        handledNums = [1]
        for i in range(n):
            handledNums.append(handledNums[i+1]+[i])
            return