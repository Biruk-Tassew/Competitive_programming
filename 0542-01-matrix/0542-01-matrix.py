class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [[float('inf')]*(len(mat[0])+2) for _ in range(len(mat)+2)]
        
        for row in range(1, len(mat)+1):
            for col in range(1, len(mat[0])+1):
                
                if not mat[row-1][col-1]:
                    dp[row][col] = 0
                else:
                    dp[row][col] = min(dp[row][col], dp[row][col-1]+1, dp[row-1][col]+1)
                    
        for row in range(len(mat), 0, -1):
            for col in range(len(mat[0]), 0, -1):
                if not mat[row-1][col-1]:
                    dp[row][col] = 0
                else:
                    dp[row][col] = min(dp[row][col], dp[row][col+1]+1, dp[row+1][col]+1)
        
                
        return [row[1:-1] for row in dp[1:-1]]