class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.memo = defaultdict(lambda:-1)
        self.matrix = matrix
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
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
        
        max_val = 0
        for i in self.directions:
            max_val = max(max_val, self.solve(row+i[0], col+i[1], self.matrix[row][col]))
        
        self.memo[(row, col)] = max_val + 1
        return self.memo[(row, col)]