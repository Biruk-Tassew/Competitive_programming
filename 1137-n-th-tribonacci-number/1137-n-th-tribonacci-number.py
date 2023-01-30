class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0]*(n+1)
        return self.solve(n, memo)
    
    def solve(self, n, memo):
        if not n:
            return 0
        if n == 1 or n == 2:
            return 1
        if memo[n]:
            return memo[n]
        
        memo[n] = self.solve(n-1, memo) + self.solve(n-2, memo) + self.solve(n-3, memo)
        return memo[n]