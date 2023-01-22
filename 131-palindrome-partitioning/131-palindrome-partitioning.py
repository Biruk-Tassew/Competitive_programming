class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.backtrack(s, [])
        return self.res 
    
    def backtrack(self, s, cur_list):
        if not s:
            self.res.append(cur_list)
            
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.backtrack(s[i:], cur_list+[s[:i]])