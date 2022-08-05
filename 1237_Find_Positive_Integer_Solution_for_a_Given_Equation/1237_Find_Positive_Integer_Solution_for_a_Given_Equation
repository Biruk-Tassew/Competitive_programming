"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    """ Two pointers version """
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        left = 1
        right = 1000
        outPut = []
        
        while left <= 1000 and right > 0:
            res = customfunction.f(left, right)
            
            if res < z:
                left += 1
            elif res > z:
                right -= 1
            else:
                outPut.append([left, right])
                left += 1
                right -= 1
        
        return outPut
        

class Solution:
    """ Binaery search version """
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        outPut = []
        
        for start in range(1, 1001):
            left = 1
            right = 1000
            while left <= right:
                mid = (left+right)//2
                res = customfunction.f(start, mid)
                
                if res < z:
                    left = mid + 1
                elif res > z:
                    right = mid - 1
                else:
                    outPut.append([start, mid])
                    break
                    
        return outPut 
