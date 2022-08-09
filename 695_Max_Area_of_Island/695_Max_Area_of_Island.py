class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    area = self.dfs(grid, row, col)
                    if area > max_area:
                        max_area = area
                
                        
        return max_area
    
    def dfs(self, grid, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
            grid[row][col] = 0
            
            return 1 + self.dfs(grid, row+1, col) + self.dfs(grid, row-1, col) + self.dfs(grid, row, col+1) + self.dfs(grid, row, col-1)
        return 0
