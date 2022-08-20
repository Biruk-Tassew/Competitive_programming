class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        que = deque([])
        fresh = 0
        minutes = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    que.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
                    
        while que and fresh:
            minutes += 1
            for i in range(len(que)):
                row, col = que.popleft()
                for i in directions:
                    n_r = row + i[0]
                    n_c = col + i[1]
                    if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and grid[n_r][n_c]==1:
                        fresh -= 1
                        grid[n_r][n_c] = 2
                        que.append((n_r, n_c))
                        
        if not fresh:
            return minutes
        return -1
                        
            
