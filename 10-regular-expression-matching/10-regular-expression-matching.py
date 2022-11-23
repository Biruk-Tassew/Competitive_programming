class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.memo = defaultdict(lambda:-1)
        return self.solve(0, 0)
    
    def solve(self, p_idx, s_idx):
        if p_idx == len(self.p):
            return len(self.s) == s_idx
        
        if self.memo[(s_idx, p_idx)] != -1:
            return self.memo[(s_idx, p_idx)]
        
        matching = s_idx < len(self.s) and self.p[p_idx] in {self.s[s_idx], "."}
        
        if p_idx < len(self.p)-1 and self.p[p_idx+1] == "*":
            ans = (matching and self.solve(p_idx, s_idx+1) or (self.solve(p_idx+2, s_idx)))
        else:
            ans = matching and self.solve(p_idx+1, s_idx+1)
            
        self.memo[(s_idx, p_idx)] = ans
        return self.memo[(s_idx, p_idx)]