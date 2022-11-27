class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        ppl_grid = [[-1]*(len(grid[0])) for _ in range(len(grid))]
        ppl_grid = self.person_traversal(grid, ppl_grid)
        fire_grid = [[-1]*(len(grid[0])) for _ in range(len(grid))]
        fire_grid = self.fire_traversal(grid, fire_grid)
        
        
        ppl_arrival = ppl_grid[-1][-1]
        fire_arrival = fire_grid[-1][-1]
        
        # Some edge cases.
        if ppl_arrival == -1:
            return -1
        if fire_arrival == -1:
            return 10 ** 9
        if fire_arrival < ppl_arrival:
            return -1

        # Whether we are 'followed' by fire on both two pathes toward bot-right cell.
        diff = fire_arrival - ppl_arrival
        ppl_1, ppl_2 = ppl_grid[-1][-2], ppl_grid[-2][-1]
        
        fire_1, fire_2 = fire_grid[-1][-2], fire_grid[-2][-1]
        if ppl_1 > -1 and ppl_2 > -1 and (fire_1 - ppl_1 > diff or fire_2 - ppl_2 > diff):
            return diff
        return diff - 1

        
        
    def person_traversal(self, grid, ppl_grid):
        que = deque([(0, 0)])
        visited = set([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 1
        
        while que:
            for i in range(len(que)):
                row, col = que.popleft()
                ppl_grid[row][col] = level
                
                for i in directions:
                    n_r = row + i[0]
                    n_c = col + i[1]
                    
                    if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and not grid[n_r][n_c] and ppl_grid[n_r][n_c] == -1: 
                        que.append((n_r, n_c))
                        
            level += 1
            
        return ppl_grid
    
    def fire_traversal(self, grid, fire_grid):
        que = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    que.append((row, col))
       
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 1
        
        while que:
            for i in range(len(que)):
                row, col = que.popleft()
                fire_grid[row][col] = level
                
                for i in directions:
                    n_r = row + i[0]
                    n_c = col + i[1]
                    
                    if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and not grid[n_r][n_c] and fire_grid[n_r][n_c] == -1:
                        que.append((n_r, n_c))
                        
            level += 1
            
        return fire_grid
    