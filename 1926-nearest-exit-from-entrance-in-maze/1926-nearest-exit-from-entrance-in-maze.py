class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        que = deque([entrance])
        level = 0
        while que:
            for _ in range(len(que)):
                row, col = que.popleft()
                
                if (not row*col or row == len(maze)-1 or col == len(maze[0])-1) and [row, col] != entrance:
                    return level
                
                for i in directions:
                    n_r = row+i[0]
                    n_c = col+i[1]
                    
                    if 0 <= n_r < len(maze) and 0 <= n_c < len(maze[0]) and maze[n_r][n_c] == ".":
                        que.append([n_r, n_c])
                        maze[n_r][n_c] = "V"
            level += 1
            
        return -1