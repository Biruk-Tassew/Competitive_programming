class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        left = 0
        right = 10**6
        
        while left < right:
            mid = (left+right)//2
            
            if self.bfs(0, 0, mid, heights):
                right = mid
            else:
                left = mid + 1
                
        return left
                
        
    def bfs(self, row, col, cur_max, heights):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        que = deque([(row, col)])
        visited = set([(row, col)])
        
        while que:
            row, col = que.popleft()
            
            if row == len(heights)-1 and col == len(heights[0])-1:
                        return True
            
            for i in directions:
                n_r = row + i[0]
                n_c = col + i[1]
                
                if 0 <= n_r < len(heights) and 0 <= n_c < len(heights[0]) and abs(heights[n_r][n_c]-heights[row][col]) <= cur_max and (n_r, n_c) not in visited:
                    
                    visited.add((n_r, n_c))
                    que.append((n_r, n_c))
                    
        return False
            