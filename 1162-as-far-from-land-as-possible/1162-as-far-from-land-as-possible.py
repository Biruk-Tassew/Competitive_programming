class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        que = deque()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    que.append([row, col])
        
        
        seen = set()
        level = 0
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()
                
                for i in directions:
                    n_row = row + i[0]
                    n_col = col + i[1]
                    
                    if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                        if (n_row, n_col) not in seen and not grid[n_row][n_col]:
                            que.append((n_row, n_col))
                            seen.add((n_row, n_col))
                            
            level += 1
            
        if level <= 1:
            return -1
        return level-1
            
        