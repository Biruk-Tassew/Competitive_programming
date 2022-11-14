class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        island_no = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    island_no += 1
                    self.dfs(row, col)
        
        return island_no
                    
    def dfs(self, cur_r, cur_c):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.grid[cur_r][cur_c] = "0"
        
        
        for i in directions:
            n_r = cur_r + i[0]
            n_c = cur_c + i[1]
            
            if 0 <= n_r < len(self.grid) and 0 <= n_c < len(self.grid[0]) and self.grid[n_r][n_c] == "1":
                self.dfs(n_r, n_c)
                            
        