class Solution:
    def fib(self, n: int) -> int:
        if n > 1:
            return self.fib(n - 1) + self.fib(n)
        else:
            return n
