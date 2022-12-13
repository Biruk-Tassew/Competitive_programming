class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return min(matrix[0])
        
        dp = [[float('inf')]*(len(matrix[0])) for _ in range(len(matrix))]
        dp[0] = matrix[0]
        min_sum = float('inf')
        
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                if not col:
                    dp[row][col] = min(dp[row][col], matrix[row][col]+dp[row-1][col], matrix[row][col]+dp[row-1][col+1])
                elif col == len(matrix[0])-1:
                    dp[row][col] = min(dp[row][col], matrix[row][col]+dp[row-1][col], matrix[row][col]+dp[row-1][col-1])
                else:
                    dp[row][col] = min(dp[row][col], matrix[row][col]+dp[row-1][col], matrix[row][col]+dp[row-1][col-1], matrix[row][col]+dp[row-1][col+1])
                    
                if row == len(matrix)-1:
                    min_sum = min(min_sum, dp[row][col])
                    
        return min_sum