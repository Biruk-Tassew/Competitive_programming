class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = defaultdict(lambda:-1)
        return self.dfs(m-1, n-1)
    
    def dfs(self, row, col):
        if row < 0 or col < 0:
            return 0
        if not row or not col:
            return 1
        
        if self.memo[(row, col)] != -1:
            return self.memo[(row, col)] 
        
        res = self.dfs(row-1, col) + self.dfs(row, col-1)
        self.memo[(row, col)] = res
        return self.memo[(row, col)] 