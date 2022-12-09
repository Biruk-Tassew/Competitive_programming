class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.directions = [(0, 1), (1, 0)]
        self.memo = defaultdict(lambda: -1)
        self.grid = grid 
        return self.dfs(0, 0)
    
    def dfs(self, row, col):
        if row == len(self.grid)-1 and col == len(self.grid[0])-1:
            return self.grid[row][col]
        if row >= len(self.grid) or col >= len(self.grid[0]):
            return float('inf')
        
        if self.memo[(row, col)] != -1:
            return self.memo[(row, col)]
        
        res =  min(self.dfs(row+1, col), self.dfs(row, col+1)) +self.grid[row][col]
    
        self.memo[(row, col)] = res 
        return self.memo[(row, col)]