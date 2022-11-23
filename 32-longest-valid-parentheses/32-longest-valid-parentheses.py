class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        max_len = 0
        
        for i in range(1, len(s)):
            cur_longest = dp[i-1]
            
            if s[i] == ")" and i-cur_longest-1 >= 0 and s[i-cur_longest-1] == "(":
                prev_longest = 0
                
                if i-cur_longest-2 >= 0:
                    prev_longest = dp[i-cur_longest-2]
                
                dp[i] = cur_longest + prev_longest + 2
                
            max_len = max(max_len, dp[i])
            
        return max_len
                
            