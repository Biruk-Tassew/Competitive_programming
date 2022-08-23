# BFS + binary search
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def bfs(grid, time):
            
            visited  = set((0,0))
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            cur_level = max(grid[0][0], time)
            que = deque([(cur_level,0,0)])
            
            while que:
                cur_level, cor_x, cor_y = que.popleft()
                
                if cor_x == len(grid)-1  and cor_y == len(grid)-1:
                    return True
                
                for i in directions:
                    n_x = cor_x + i[0]
                    n_y = cor_y + i[1]
                    
                    
                    if 0 <= n_x < len(grid) and 0 <= n_y < len(grid) and (n_x,n_y) not in visited:
                        new_level = max(grid[n_x][n_y], time)
                        if new_level==cur_level:
                            visited.add((n_x,n_y))
                            que.append((new_level,n_x,n_y))
                    
                                 
        left = 0
        right = (len(grid))**2
        ans = None
        while left <= right:
            m = (left+right)//2
            
            if bfs(grid, m):
                ans = m
                right = m-1
            else:
                left = m+1
                
        return ans
                
            
# not sure if this is fully BFS
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, (grid[0][0],0,0))
        visited  = set((0,0))
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        water_level = grid[0][0]
        
        while heap:
            cur_level, cor_x, cor_y = heapq.heappop(heap)
            water_level = max(water_level, cur_level)
            if cor_x == len(grid)-1  and cor_y == len(grid)-1:
                return water_level
            
            for i in directions:
                n_x = cor_x + i[0]
                n_y = cor_y + i[1]
                
                if 0 <= n_x < len(grid) and 0 <= n_y < len(grid) and (n_x,n_y) not in visited:
                    visited.add((n_x,n_y))
                    heapq.heappush(heap, (grid[n_x][n_y],n_x,n_y))
                
                             
        return water_level
