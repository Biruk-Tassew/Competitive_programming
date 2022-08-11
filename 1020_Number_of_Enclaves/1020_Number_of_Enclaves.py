class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not row*col or row == len(grid)-1 or col == len(grid[0])-1 and grid[row][col]:
                    self.dfs(grid, row, col)
                    
        safe_land = 0
        for i in grid:
            safe_land += sum(i)
            
        return safe_land
        
        
    def dfs(self, board, row, col):
        direction = [(0,1), (1,0), (0,-1), (-1, 0)]
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col]:
            board[row][col] = 0
            for i in direction:
                self.dfs(board, row+i[0], col+i[1])
            
