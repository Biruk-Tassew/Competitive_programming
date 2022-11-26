class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        left = 0
        right = len(grid)**2
        ans = None
        
        while left <= right:
            mid = (left+right)//2
            
            if self.bfs(0, 0, grid, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
        
    def bfs(self, row, col, grid, time):
        que = deque([(row, col, max(time, grid[row][col]))])
                     
        visited = set([(row, col)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while que:
            row, col, cur_time = que.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1:
                return True
        
            for i in directions:
                n_r = row+i[0]
                n_c = col+i[1]
                
                if 0 <= n_r < len(grid) and 0 <= n_c < len(grid[0]) and (n_r, n_c) not in visited:
                    n_time = max(grid[n_r][n_c], time)
                    if n_time == cur_time:
                        que.append((n_r, n_c, n_time))
                        visited.add((n_r, n_c))
                        
                    
                