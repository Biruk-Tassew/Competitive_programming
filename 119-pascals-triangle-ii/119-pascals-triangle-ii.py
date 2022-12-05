class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        dp = [[1], [1,1]]
        
        for i in range(2, rowIndex+1):
            n_row = [1]
            
            for j in range(1, i):
                n_row.append(dp[i-1][j]+dp[i-1][j-1])
                
            dp.append(n_row+[1])
            
        return dp[rowIndex]