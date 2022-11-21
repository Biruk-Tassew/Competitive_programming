class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.memo = defaultdict(bool)
        return self.solve(0, 0)
    
    def solve(self, t_idx, p_idx):
        if p_idx == len(self.p):
            return t_idx == len(self.s)
        
            
        if self.memo[(t_idx, p_idx)]:
            return self.memo[(t_idx, p_idx)]
        
        match = t_idx < len(self.s) and self.p[p_idx] in [self.s[t_idx], "."]
        
        if p_idx < len(self.p)-1 and self.p[p_idx+1] == "*":
            ans = self.solve(t_idx, p_idx+2) or (match and self.solve(t_idx+1, p_idx))
        else:
            ans = match and self.solve(t_idx+1, p_idx+1)
            
        self.memo[(t_idx, p_idx)] = ans 
        return self.memo[(t_idx, p_idx)]