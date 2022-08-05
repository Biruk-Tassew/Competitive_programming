class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for i in grid:
            left = 0
            right = len(i)-1
            
            while left <= right:
                mid = (left+right)//2
                
                if i[mid] >= 0:
                    left = mid + 1
                elif left != right and i[mid-1] < 0:
                    right = mid
                else:
                    if left != right and i[mid-1] >= 0:
                        left = mid
                    count += len(i[left:])
                    break
            
                    
        return count
                    
                    
