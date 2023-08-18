class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[float('inf')]*len(mat[0]) for _ in range(len(mat))]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        que = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if not mat[row][col]:
                    que.append((row, col))
                    ans[row][col] = 0
                
        
        level = 0
        seen = set()
        while que:
            
            for _ in range(len(que)):
                row, col = que.popleft()
                
                for i in directions:
                    n_r = row+i[0]
                    n_c = col+i[1]
                    
                    if 0<=n_r<len(mat) and 0<=n_c<len(mat[0]) and ans[n_r][n_c] > ans[row][col] + 1:
                        que.append((n_r, n_c))
                        ans[n_r][n_c] = ans[row][col] + 1
            level += 1
            
        return ans
                        
                    
            