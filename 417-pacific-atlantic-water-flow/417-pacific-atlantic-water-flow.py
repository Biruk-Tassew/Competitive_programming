class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_inits = [(i, 0) for i in range(len(heights))]+[(0, i) for i in range(len(heights[0]))]
        atlantic_inits = [(i, len(heights[0])-1) for i in range(len(heights))]+[(len(heights)-1, i) for i in range(len(heights[0]))]
        
        return self.bfs(heights, pacific_inits)&self.bfs(heights, atlantic_inits)

    def bfs(self, heights, init_pos):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        que = deque(init_pos)
        visited = set(init_pos)
        
        while que:
            row, col = que.popleft()
            
            for i in directions:
                n_r = row+i[0]
                n_c = col+i[1]
                
                if 0<=n_r<len(heights) and 0<=n_c<len(heights[0]) and heights[n_r][n_c] >= heights[row][col] and (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    que.append((n_r, n_c))
                    
                    
        return visited