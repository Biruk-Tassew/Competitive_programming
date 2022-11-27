class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        pt = 1
        
        for i in range(1, len(s)):
            if ord(s[i])-ord(s[i-1]) == 1:
                pt += 1
            else:
                pt = 1
            max_len = max(max_len, pt)
                
        return max_len