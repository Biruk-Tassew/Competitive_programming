class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        seen = set()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if board[row][col]+"in row"+str(row) in seen or\
                       board[row][col]+"in col"+str(col) in seen or\
                       board[row][col]+str(row//3)+str(col//3) in seen:
                        return False
                    seen.add(board[row][col]+"in row"+str(row))
                    seen.add(board[row][col]+"in col"+str(col))
                    seen.add(board[row][col]+str(row//3)+str(col//3))
                    
        return True
                
            
        
        
        