class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = defaultdict(lambda:-1)
        return self.solve(0, 0, text1, text2)
        
    def solve(self, idx_one, idx_two, text1, text2):
        if idx_one == len(text1) or idx_two == len(text2):
            return 0
        
        if self.memo[(idx_one, idx_two)] != -1:
            return self.memo[(idx_one, idx_two)]
        
        if text1[idx_one] == text2[idx_two]:
            self.memo[(idx_one, idx_two)] = self.solve(idx_one+1, idx_two+1, text1, text2) + 1
            return self.memo[(idx_one, idx_two)]
        
        self.memo[(idx_one, idx_two)] = max(self.solve(idx_one+1, idx_two, text1, text2), self.solve(idx_one, idx_two+1, text1, text2))
        
        return self.memo[(idx_one, idx_two)]