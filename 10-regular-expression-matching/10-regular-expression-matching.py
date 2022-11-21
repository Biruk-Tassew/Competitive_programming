class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s 
        self.p = p
        self.memo = defaultdict(bool)
        return self.solve(0, 0)
        
        
    def solve(self, s_idx, p_idx):
        if p_idx == len(self.p):
            return s_idx == len(self.s)
        
        if self.memo[(p_idx, s_idx)]:
            return self.memo[(s_idx, p_idx)]
        
        matching = s_idx < len(self.s) and self.p[p_idx] in {self.s[s_idx], "."}
        
        if p_idx < len(self.p)-1 and self.p[p_idx+1] == "*":
            ans = (matching and self.solve(s_idx+1, p_idx)) or self.solve(s_idx, p_idx+2)
        else:
            ans = matching and self.solve(s_idx+1, p_idx+1)
            
        self.memo[(s_idx, p_idx)] = ans
        return self.memo[(s_idx, p_idx)]