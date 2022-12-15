class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.memo = defaultdict(lambda:-1)
        return self.solve(0, len(s)-1, s)
    
    def solve(self, left_idx, right_idx, s):
        if left_idx == right_idx:
            return 1
        if left_idx > right_idx:
            return 0
        if self.memo[(left_idx, right_idx)] != -1:
            return self.memo[(left_idx, right_idx)]
        res = 0 
        if s[left_idx] == s[right_idx]:
            self.memo[(left_idx, right_idx)] = self.solve(left_idx+1, right_idx-1, s) + 2
            return self.memo[(left_idx, right_idx)]
            
        
        self.memo[(left_idx, right_idx)] = max(self.solve(left_idx+1, right_idx, s), self.solve(left_idx, right_idx-1, s))
        return self.memo[(left_idx, right_idx)]
        
            
        