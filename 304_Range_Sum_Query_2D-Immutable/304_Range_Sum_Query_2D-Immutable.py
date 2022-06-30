class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix[0]) + 1
        column = len(matrix) + 1
        self.sum_ = [[0] * row for _ in range(column)]
        
        for i in range(1, column):
            for j in range(1, row):
                self.sum_[i][j] = matrix[i-1][j-1] + self.sum_[i-1][j] + self.sum_[i][j-1] - self.sum_[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_[row2+1][col2+1] - self.sum_[row2+1][col1] - self.sum_[row1][col2+1] + self.sum_[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
