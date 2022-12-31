class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.path_len = 0
        self.count_path = 0
        starting_cor = (0,0)
        self.grid = grid
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != -1:
                    self.path_len += 1
                
                if grid[row][col] == 1:
                    starting_cor = (row, col)
          

        self.back_track(starting_cor[0], starting_cor[1], [starting_cor])
        return self.count_path
        
    def back_track(self, row, col, cur_path):
        if self.grid[row][col] == 2:
            if len(cur_path) == self.path_len:
                self.count_path += 1
            return 
        
        for i in self.directions:
            n_r = row + i[0]
            n_c = col + i[1]
            
            if 0 <= n_r < len(self.grid) and 0 <= n_c < len(self.grid[0]) and (n_r, n_c) not in cur_path and self.grid[n_r][n_c] != -1:
                cur_path.append((n_r, n_c))
                
                self.back_track(n_r, n_c, cur_path)
                
                cur_path.pop()