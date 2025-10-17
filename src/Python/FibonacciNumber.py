class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n

        dp = []
        dp.append(0)
        dp.append(1)
        for i in range(2, n+1):
            ssum = dp[i-1] + dp[i-2]
            dp.append(ssum)
        return dp[-1]