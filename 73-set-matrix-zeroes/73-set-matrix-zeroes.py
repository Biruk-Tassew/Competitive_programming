class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    zero_rows.add(row)
                    zero_cols.add(col)
                    
        for row in zero_rows:
            matrix[row] = [0]*len(matrix[0])
            
        for col in zero_cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
            
        
                    