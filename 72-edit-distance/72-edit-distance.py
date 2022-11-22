class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        
        for col in range(len(word1)+1):
            dp[0][col] = col
        for row in range(len(word2)+1):
            dp[row][0] = row
            
        for row in range(1, len(word2)+1):
            for col in range(1, len(word1)+1):
                if word1[col-1] == word2[row-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    insert = dp[row][col-1] + 1
                    delete = dp[row-1][col] + 1
                    replace = dp[row-1][col-1] + 1
                    dp[row][col] = min(insert, delete, replace)
                            
        return dp[-1][-1]