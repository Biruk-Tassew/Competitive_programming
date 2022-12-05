class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = set(wordDict)
        self.memo = defaultdict(lambda: -1)
        return self.solve(0, s)
        
    def solve(self, st_idx, s):
        if st_idx == len(s):
            return True
        
        if self.memo[st_idx] != -1:
            return self.memo[st_idx]
        
        for i in range(st_idx, len(s)):
            if s[st_idx:i+1] in self.wordDict:
                if self.solve(i+1, s):
                    self.memo[st_idx] = True
                    return self.memo[st_idx]
                
        self.memo[st_idx] = False
        return self.memo[st_idx]