class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(n)
    
    @cache
    def solve(self, n):
        if n <= 0:
            return 0
        if n <= 2:
            return n
        
        return self.solve(n-1)+self.solve(n-2)