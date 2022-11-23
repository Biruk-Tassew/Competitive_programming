class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            temp_board = []
            for j in board[i]:
                if j.isdigit():
                    temp_board.append(j)
            if len(set(temp_board)) != len(temp_board):
                return False
            
        
        for j in zip(*board):
            temp_board = []
            for k in j:
                if k.isdigit():
                    temp_board.append(k)
            if len(set(temp_board)) != len(temp_board):
                return False
        
        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                square = [board[x][y] for x in range(row, row + 3) for y in range(col, col + 3)]
               
                square = [i for i in square if i != '.']
                if len(set(square)) != len(square):
                    return False
        return True
            
        
        
        