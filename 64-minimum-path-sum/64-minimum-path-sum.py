class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.directions = [(0, 1), (1, 0)]
        self.memo = defaultdict(lambda:-1)
        self.grid = grid
        return self.solve(0, 0)
    
    def solve(self, row, col):
        if row == len(self.grid)-1 and col == len(self.grid[0])-1:
            return self.grid[row][col]
        
        if self.memo[(row, col)] != -1:
            return self.memo[(row, col)]
        
        res = float('inf')
        for i in self. directions:
            n_r = row + i[0]
            n_c = col + i[1]
            
            if 0<=n_r<len(self.grid) and 0<=n_c<len(self.grid[0]):
                res = min(res, self.solve(n_r, n_c)+self.grid[row][col])
        
        
        self.memo[(row, col)] = res 
        return self.memo[(row, col)]