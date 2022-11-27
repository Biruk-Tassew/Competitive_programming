class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        dp = 1
        
        for i in range(1, len(s)):
            if ord(s[i])-ord(s[i-1]) == 1:
                dp += 1
            else:
                dp = 1
            max_len = max(max_len, dp)
                
        return max_len