class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        key_no = 0
        st_r = 0
        st_c = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col].islower():
                    key_no += 1
                    
                if grid[row][col] == "@":
                    st_r = row
                    st_c = col
                    
        seen = set((st_r, st_c, "")) 
        que = deque([(st_r, st_c, "")])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        level = 0
        while que:
            for _ in range(len(que)):
                
                row, col, cur_keys = que.popleft()
                
                if len(cur_keys) == key_no:
                    return level
                
                for i in directions:
                    n_r = row + i[0]
                    n_c = col + i[1]
                    
                    if 0 <= n_r < len(grid) and 0<= n_c < len(grid[0]) and grid[n_r][n_c] != "#":
                        if grid[n_r][n_c].isupper() and grid[n_r][n_c].lower() not in cur_keys:
                            continue
                            
                        n_key = cur_keys
                        if grid[n_r][n_c].islower() and grid[n_r][n_c] not in cur_keys:
                            n_key+=grid[n_r][n_c]
                            
                            
                        if (n_r, n_c, n_key) not in seen:
                            que.append((n_r, n_c, n_key))
                            seen.add((n_r, n_c, n_key))
                                
            level += 1
            
            
        return -1

                            
                    
                    