class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0]+horizontalCuts+[h]
        verticalCuts = [0]+verticalCuts+[w]
        
        max_height = max([(verticalCuts[i+1]-verticalCuts[i], i) for i in range(len(verticalCuts)-1)])
        max_width = max([(horizontalCuts[i+1]-horizontalCuts[i], i) for i in range(len(horizontalCuts)-1)])
        
        return (max_width[0]*max_height[0])%(10**9 + 7)