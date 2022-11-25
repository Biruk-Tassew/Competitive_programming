class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        abs_max = 0
        abs_min = float('inf')
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                abs_min = min(abs_min, heights[row][col])
                abs_max = max(abs_max, heights[row][col])
                
        left = 0
        right = abs_max-abs_min
        
        while left < right:
            mid = (left+right)//2
            
            if self.bfs(0, 0, mid, heights):
                right = mid
            else:
                left = mid + 1
                
        return right
                
        
    def bfs(self, row, col, cur_max, heights):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        que = deque([(row, col)])
        visited = set()
        
        while que:
            row, col = que.popleft()
            
            for i in directions:
                n_r = row + i[0]
                n_c = col + i[1]
                
                if 0 <= n_r < len(heights) and 0 <= n_c < len(heights[0]) and abs(heights[n_r][n_c]-heights[row][col]) <= cur_max and (n_r, n_c) not in visited:
                    if n_r == len(heights)-1 and n_c == len(heights[0])-1:
                        return True
                    
                    visited.add((n_r, n_c))
                    que.append((n_r, n_c))
                    
        return False
            