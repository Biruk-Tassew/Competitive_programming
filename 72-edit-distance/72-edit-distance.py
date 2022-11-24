class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        self.word1 = word1
        self.word2 = word2
        self.memo = defaultdict(lambda :-1)
        return self.solve(0, 0)
    
    def solve(self, idx_one, idx_two):
        if idx_one == len(self.word1):
            if idx_two == len(self.word2):
                return 0
            else:
                return len(self.word2)-idx_two
            
        if idx_two == len(self.word2):
            return len(self.word1)-idx_one
        
        if self.memo[(idx_one, idx_two)] != -1:
            return self.memo[(idx_one, idx_two)]
      
        
        if self.word1[idx_one] == self.word2[idx_two]:
            ans = self.solve(idx_one+1, idx_two+1)
        else:
            insert = self.solve(idx_one, idx_two+1)+1
            delete = self.solve(idx_one+1, idx_two)+1
            replace = self.solve(idx_one+1, idx_two+1)+1
            ans = min(insert, delete, replace)
            
        self.memo[(idx_one, idx_two)] = ans
        return self.memo[(idx_one, idx_two)]