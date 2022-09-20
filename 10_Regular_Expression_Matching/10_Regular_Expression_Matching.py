class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        
        for i in range(len(p)):
            if p[i] == "*":
                dp[0][i+1] = dp[0][i-1]
                
                
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == "*":
                    dp[i+1][j+1] = dp[i+1][j-1] or ((p[j-1] == "." or s[i] == p[j-1]) and dp[i][j+1])
                
                elif p[j] == "." or s[i] == p[j]:
                    dp[i+1][j+1] = dp[i][j]
        
        return dp[-1][-1]
                    
