class Solution:
    def fib(self, n: int) -> int:
        # def fibCalc(n):
        #     if not n or n == 1:
        #         return n
        #     else:
        #         return fibCalc(n-1) + fibCalc(n-2)
        # return fibCalc(n)
        dp = [0]*(n+1)
        if n >= 1:
            dp[1] = 1
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
