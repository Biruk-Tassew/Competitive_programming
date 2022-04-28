class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 2:
            return min(height[0], height[1]) 
        maxArea = 0
        firstIdx = 0
        lastIdx = len(height) - 1
        
        while lastIdx - firstIdx >= 1:
            
            if min(height[firstIdx], height[lastIdx]) * (lastIdx - firstIdx) > maxArea:
                maxArea = min(height[firstIdx], height[lastIdx]) * (lastIdx - firstIdx)
        
            if height[firstIdx] < height[lastIdx]:
                firstIdx += 1
            else:
                lastIdx -= 1
            
                
        return maxArea
