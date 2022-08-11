class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.directions = [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        self.dfs(board, click[0], click[1])
        return board
    
    def dfs(self, board, row, col):
        mines_count = 0
        for i in range(8):
            n_row = row + self.directions[i][0]
            n_col = col + self.directions[i][1]
            if 0 <= n_row < len(board) and 0 <= n_col < len(board[0]) and board[n_row][n_col] == 'M':
                mines_count += 1
                
        if mines_count:
            board[row][col] = str(mines_count)
        else:
            board[row][col] = 'B'
            for i in range(8):
                n_row = row + self.directions[i][0]
                n_col = col + self.directions[i][1]
                if 0 <= n_row < len(board) and 0 <= n_col < len(board[0]) and board[n_row][n_col] == 'E':
                    self.dfs(board, n_row, n_col)
                
