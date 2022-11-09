class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        self.solve(s, "", 0)
        return self.res
    def solve(self, s, cur_s, idx):
        if idx == len(s):
            self.res.append(cur_s)
            cur_s = cur_s[:-1]
            
            return 
            
        if s[idx].islower():
            cur_s += s[idx].upper()
            self.solve(s, cur_s, idx+1)
            cur_s = cur_s[:-1]
        elif s[idx].isupper():
            cur_s += s[idx].lower()
            self.solve(s, cur_s, idx+1)
            cur_s = cur_s[:-1]
            
        self.solve(s, cur_s+s[idx], idx+1)
                
                
            