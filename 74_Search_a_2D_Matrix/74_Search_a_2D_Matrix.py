class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        store = []
        
        for i in matrix:
            for j in i:
                store.append(j)
                
        left = 0 
        right = len(store)-1
        
        while left <= right:
            mid = (left+right)//2
            
            if store[mid] < target:
                left = mid + 1
            elif store[mid] > target:
                right = mid - 1
            else:
                return True
        return False
      
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ With a constant space complexity """
        
        left = 0 
        right = len(matrix)*len(matrix[0])-1
        
        while left <= right:
            mid = (left+right)//2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
        return False
