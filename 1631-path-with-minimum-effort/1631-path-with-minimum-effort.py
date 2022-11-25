class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        all_efforts = [[float('inf')]*len(heights[0]) for _ in range(len(heights))]
        all_efforts[0][0] = 0
        heap = [(0, 0, 0)]
        
        while heap:
            cur_effort, row, col = heapq.heappop(heap)
            
            if row==len(heights)-1 and col==len(heights[0])-1:
                return cur_effort
            
            for i in directions:
                n_r = row+i[0]
                n_c = col+i[1]
                
                if 0 <= n_r < len(heights) and 0 <= n_c < len(heights[0]):
                    n_effort = max(cur_effort, abs(heights[row][col]-heights[n_r][n_c]))
                    if n_effort < all_efforts[n_r][n_c]:
                        all_efforts[n_r][n_c] = n_effort
                        heapq.heappush(heap, (n_effort, n_r, n_c))