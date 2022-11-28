class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0]*(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        
        for s_idx in range(len(s), -1, -1):
            for p_idx in range(len(p)-1, -1, -1):
                
                matching = s_idx < len(s) and p[p_idx] in {s[s_idx], "."}
                if p_idx < len(p)-1 and p[p_idx+1] == "*":
                    dp[s_idx][p_idx] = dp[s_idx][p_idx+2] or (matching and dp[s_idx+1][p_idx])
                else:
                    dp[s_idx][p_idx] = matching and dp[s_idx+1][p_idx+1]
                
        return dp[0][0]
        