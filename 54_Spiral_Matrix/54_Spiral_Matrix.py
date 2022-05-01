class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def cleaner(matrix):
            return list(filter(([]).__ne__, matrix))
        outPut = []
        
        while matrix:
            if [] in matrix:
                    matrix = cleaner(matrix)
            if matrix:
                for i in matrix[0]:
                    outPut.append(i)
                matrix.remove(matrix[0])
            if [] in matrix:
                    matrix = cleaner(matrix)
            if matrix:
                for i in matrix:
                    outPut.append(i[-1])
                    i.remove(i[-1])
            if [] in matrix:
                    matrix = cleaner(matrix)
            if matrix:
                for i in range(-1, -1*len(matrix[0])-1, -1):
                    outPut.append(matrix[-1][i])
                matrix.remove(matrix[-1])
                if [] in matrix:
                    matrix = cleaner(matrix)
                for i in range(-1, -1*len(matrix)-1, -1):
                    outPut.append(matrix[i][0])
                    matrix[i].remove(matrix[i][0])
        return outPut
