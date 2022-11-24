class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.memo = defaultdict(lambda :-1)
        return self.solve(0, 0)
    
    def solve(self, s_idx, p_idx):
        if p_idx == len(self.p):
            return len(self.s) == s_idx
        
        if self.memo[(s_idx, p_idx)] != -1:
            return self.memo[(s_idx, p_idx)]
        
        ans = False
        if s_idx < len(self.s) and (self.s[s_idx] == self.p[p_idx] or self.p[p_idx] == "?"):
            ans = self.solve(s_idx+1, p_idx+1)
        elif self.p[p_idx] == "*":
            ans = self.solve(s_idx, p_idx+1) or (s_idx < len(self.s) and self.solve(s_idx+1, p_idx))
        
        self.memo[(s_idx, p_idx)] = ans
        return self.memo[(s_idx, p_idx)]