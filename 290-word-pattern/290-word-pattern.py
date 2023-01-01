class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        for i in range(len(s)):
            if pattern.index(pattern[i]) != s.index(s[i]):
                return False
            
        return True