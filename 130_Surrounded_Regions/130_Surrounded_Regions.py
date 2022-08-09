class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if not row or not col or row == len(board)-1 or col == len(board[0])-1:
                    self.dfs(board, row, col)
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'V':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
                
        
    def dfs(self, board, row, col):
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
            board[row][col] = 'V' # V is for visited
            
            self.dfs(board, row+1, col)
            self.dfs(board, row-1, col)
            self.dfs(board, row, col+1)
            self.dfs(board, row, col-1)
     
