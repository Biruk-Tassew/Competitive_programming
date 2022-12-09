class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.memo = defaultdict(lambda:-1)
        self.matrix = matrix
        ans = -1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ans = max(ans, self.solve(row, col, -1))
                
        return ans
        
    def solve(self, row, col, prev):
        if row < 0 or col < 0 or row >= len(self.matrix) or col >= len(self.matrix[0]) or self.matrix[row][col] <= prev:
            return 0
        
        if self.memo[(row, col)] != -1:
            return self.memo[(row, col)]
        
        left = self.solve(row, col-1, self.matrix[row][col])
        right = self.solve(row, col+1, self.matrix[row][col])
        up = self.solve(row-1, col, self.matrix[row][col])
        down = self.solve(row+1, col, self.matrix[row][col])
        
        self.memo[(row, col)] = max(left, right, up, down) + 1
        return self.memo[(row, col)]