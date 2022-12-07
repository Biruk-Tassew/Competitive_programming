class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        que = deque()
        if not grid[0][0]:
            que.append((0, 0))
        visited = set()
        level = 1
        while que:
            
            for i in range(len(que)):
                row, col = que.popleft()
                
                if (row, col) == (len(grid)-1, len(grid[0])-1):
                    return level
                
                for i in directions:
                    n_r = row+i[0]
                    n_c = col+i[1]
                    
                    if 0<=n_r<len(grid) and 0<=n_c<len(grid[0]) and (n_r, n_c) not in visited and not grid[n_r][n_c]:
                        visited.add((n_r, n_c))
                        que.append((n_r, n_c))
                        
            level += 1
            
        return -1
                    
                
                