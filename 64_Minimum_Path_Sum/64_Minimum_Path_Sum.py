# Top-down 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1]*len(grid[0]) for _ in range(len(grid))]
        return self.solve(grid, len(grid)-1, len(grid[0])-1, memo)
        
    def solve(self, grid, row, col, memo):
        if row == 0 and col == 0:
            return grid[row][col]
        
        if memo[row][col] != -1:
            return  memo[row][col]
        
        if not row:
            return grid[row][col] + self.solve(grid, row, col-1, memo)
        if not col:
            return grid[row][col] + self.solve(grid, row-1, col, memo)
        
        memo[row][col] = grid[row][col] + min(self.solve(grid, row-1, col, memo), self.solve(grid, row, col-1, memo)) 
        
        return memo[row][col]
        
# Bottom-up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not row and col:
                    grid[row][col] += grid[row][col-1]
                elif not col and row:
                    grid[row][col] += grid[row-1][col]
                elif row and col:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
                    
        return grid[-1][-1]
