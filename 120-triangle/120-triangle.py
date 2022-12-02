class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        self.memo = defaultdict(lambda:-1)
        
        return self.solve(0, 0)
    def solve(self, row, col):
        if row == len(self.triangle):
            return 0
        
        if self.memo[(row, col)] != -1:
            return self.memo[(row, col)]
        
        self.memo[(row, col)] = self.triangle[row][col] + min(self.solve(row+1, col), self.solve(row+1, col+1))
        
        return self.memo[(row, col)]