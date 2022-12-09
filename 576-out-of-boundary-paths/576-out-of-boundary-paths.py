class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.memo = defaultdict(lambda:-1)
        return self.solve(m,n,maxMove, startRow, startColumn)%(10**9 + 7)
        
    def solve(self, m, n, left_move, row, col):
        if row == m or col == n or row < 0 or col < 0:
            return 1
        
        if not left_move:
            return 0
        
        if self.memo[(row, col, left_move)] != -1:
            return self.memo[(row, col, left_move)]%(10**9 + 7)
        
        temp_val = 0
        for i in self.directions:
            temp_val += self.solve(m, n, left_move-1, row+i[0], col+i[1])%(10**9 + 7)
            
        
        self.memo[(row, col, left_move)] = temp_val
        return self.memo[(row, col, left_move)]
            