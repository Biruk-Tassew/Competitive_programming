class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        max_len = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                if not row or not col or not int(matrix[row][col]):
                    dp[row][col] = int(matrix[row][col])
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1]) + 1
                    
                max_len = max(max_len, dp[row][col])
                
        
        return max_len**2