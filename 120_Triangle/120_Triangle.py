# Bottom-up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)
        
        for row in triangle[::-1]:
            for col in range(len(row)):
                dp[col] = row[n] + min(dp[col], dp[col+1])
                
        return dp[0]
# Top-down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[-1]*len(i) for i in triangle]
        return self.solve(triangle, memo, 0, 0)
    
    def solve(self, triangle, memo, row, n):
        if row >= len(triangle):
            return 0
        
        if memo[row][n] != -1:
            return memo[row][n]
        memo[row][n] = triangle[row][n] + min(self.solve(triangle, memo, row+1, n), self.solve(triangle, memo, row+1, n+1))
        
        return memo[row][n]
