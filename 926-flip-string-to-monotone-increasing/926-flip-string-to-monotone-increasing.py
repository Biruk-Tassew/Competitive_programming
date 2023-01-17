class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        return self.solve(0, "0", s)
    
    @cache  
    def solve(self, cur_idx, prev_str, s):
        if cur_idx == len(s):
            return 0
        
        min_flip = float('inf')
        
        if prev_str == s[cur_idx]:
            min_flip = min(min_flip, self.solve(cur_idx+1, s[cur_idx], s))
        else:
            if prev_str == "1":
                min_flip = min(min_flip, self.solve(cur_idx+1, "1", s)+1)
            else:
                min_flip = min(self.solve(cur_idx+1, s[cur_idx], s), self.solve(cur_idx+1, "0", s)+1)
                
        return min_flip