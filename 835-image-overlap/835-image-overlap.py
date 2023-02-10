class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_ones = self.find_ones(img1)
        img2_ones = self.find_ones(img2)
        
        count = defaultdict(lambda :0)
        max_count = 0
        
        for i in img1_ones:
            for j in img2_ones:
                count[(j[0]-i[0], j[1]-i[1])] += 1
                max_count = max(max_count, count[(j[0]-i[0], j[1]-i[1])])
                
        return max_count
    
    def find_ones(self, matrix):
        ones = []
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col]:
                    ones.append((row, col))
                    
        return ones
            