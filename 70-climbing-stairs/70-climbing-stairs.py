class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = defaultdict(lambda :-1)
        return self.climb(n)
    def climb(self, n):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return n
        
        if self.memo[n] != -1:
            return self.memo[n]
        
        res = self.climb(n-1)+self.climb(n-2)
        self.memo[n] = res
        return self.memo[n]