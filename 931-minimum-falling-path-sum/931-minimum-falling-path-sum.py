class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_sum = float('inf')
        self.matrix = matrix
        self.memo = defaultdict(lambda:"")
        for i in range(len(matrix[0])):
            min_sum = min(min_sum, self.solve(len(matrix)-1, i))
            
        return min_sum
    
    def solve(self, row, col):
        if col < 0 or col == len (self.matrix):
            return float('inf')
        if not row:
            return self.matrix[row][col]
        
        if self.memo[(row, col)] != "":
            return self.memo[(row, col)]
        
        left_dig = self.solve(row-1, col-1)
        right_dig = self.solve(row-1, col+1)
        up = self.solve(row-1, col)
        
        res = self.matrix[row][col] + min(left_dig, right_dig, up)
        self.memo[(row, col)] = res
        return self.memo[(row, col)]