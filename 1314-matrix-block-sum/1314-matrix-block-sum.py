class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        new_matrix = [[0] * (len(mat[0]) + 1)] + [[0] + row for row in mat]
        res = [[0] * len(mat[0]) for i in range(len(mat))]

        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                new_matrix[i][j] += new_matrix[i - 1][j] + new_matrix[i][j - 1] - new_matrix[i - 1][j - 1]
                
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                n_r1, n_r2 = max(row - k, 0), min(row + k + 1, len(mat))
                n_c1, n_c2 = max(col - k, 0), min(col + k + 1, len(mat[0]))
                res[row][col] = new_matrix[n_r2][n_c2] - new_matrix[n_r2][n_c1] - new_matrix[n_r1][n_c2] + new_matrix[n_r1][n_c1]

        return res