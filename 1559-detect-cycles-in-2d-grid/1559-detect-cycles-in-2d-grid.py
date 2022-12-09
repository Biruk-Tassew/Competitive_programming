class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.color = defaultdict(lambda:"W")
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if self.color[(row, col)] == "W":
                    if self.dfs(row, col, -1, -1, grid):
                        return True
                    
        return False
    
    def dfs(self, row, col, prev_row, prev_col, grid):
        
        self.color[(row, col)] = "G"
        
        for i in self.directions:
            n_r = row+i[0]
            n_c = col+i[1]
            
            if 0<=n_r<len(grid) and 0<=n_c<len(grid[0]) and grid[n_r][n_c] == grid[row][col] and (n_r, n_c) != (prev_row, prev_col):
                if self.color[(n_r, n_c)] == "G" or (self.color[(n_r, n_c)]=="W" and self.dfs(n_r, n_c, row, col, grid)):
                    return True
        
        self.color[(row, col)] = "B"
        return False
        
        