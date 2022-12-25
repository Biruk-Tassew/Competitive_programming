class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        s = "".join(["".join(list(map(str, row))) for row in board])
        print(s)
        
        visited = set(s)
        que = deque([[s, s.index('0')]])
        level = 0
        
        while que:
            for _ in range(len(que)):
                cur_str, zero_idx = que.popleft()
                
                if cur_str == '123450':
                    return level
                
                
                
                for i in directions:
                    n_r =  zero_idx // len(board[0]) + i[0]
                    n_c = zero_idx % len(board[0]) +  i[1]
                    if 0 <= n_r < len(board) and 0 <= n_c < len(board[0]):
                        new_str = [j for j in cur_str]
                        new_str[zero_idx] = new_str[n_r * len(board[0]) + n_c]
                        new_str[n_r*len(board[0]) + n_c] = '0'
                        new_str = "".join(new_str)
                        
                        if new_str not in visited:
                            visited.add(new_str)
                            que.append([new_str, n_r*len(board[0])+n_c])
                        
            level += 1
            
        return -1