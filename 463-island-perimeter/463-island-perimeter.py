class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        self.count = 0
        directions = [(0,1),(1, 0),(-1,0),(0,-1)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    self.dfs(row, col, grid, visited, directions)
                    return self.count
        
        
    def dfs(self, row, col, grid, visited, directions):
        visited.add((row, col))
        cur_cnt = 0
        for i in directions:
            n_r = row + i[0]
            n_c = col + i[1]
            
            if (n_r, n_c) in visited:
                continue
            
            if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]):
                
                if not grid[n_r][n_c]:
                    cur_cnt += 1
                elif grid[n_r][n_c] == 1:
                    self.dfs(n_r, n_c, grid, visited, directions)
            else:
                cur_cnt += 1
            
        self.count += cur_cnt 
                
        