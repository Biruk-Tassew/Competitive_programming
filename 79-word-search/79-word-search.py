class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.board = board
        self.found = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.solve(row, col, 0, word):
                    return True
        return False
    
    def solve(self, row, col, cur_idx, word):
        if cur_idx == len(word):
            return True
        
        res = False
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]) and self.board[row][col] == word[cur_idx]:
            temp_char = self.board[row][col]
            self.board[row][col] = -1
            
            for i in self.directions:
                
                    res = res or self.solve(row+i[0], col+i[1], cur_idx+1, word)
                    
            self.board[row][col] = temp_char
            
        return res