class Solution:
    def splitString(self, s: str) -> bool:
        for i in range(len(s)-1):
            if self.backtrack(i+1, s[:i+1], s):
                return True
            
        return False
    
    def backtrack(self, start_idx, prev, s):
        if start_idx == len(s):
            return True
        
        cur_val = ""
        for i in range(start_idx, len(s)):
            cur_val += s[i]
            if int(prev)-int(cur_val) == 1 and self.backtrack(i+1, cur_val, s):
                return True
            
            
        return False
                