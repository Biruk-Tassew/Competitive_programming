class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_rect = 0
        dp = [0]*len(matrix[0])
        
        for row in matrix:
            for col in range(len(row)):
                if row[col] == "0":
                    dp[col] = 0
                else:
                    dp[col] += 1
            max_rect = max(max_rect, self.largestRectangleArea(dp))
            
        return max_rect
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        idx = 0
        max_rect = 0
        
        for i in range(len(heights)+1):
            while stack and (i==len(heights) or heights[stack[-1]] > heights[i]):
                cur_height = heights[stack.pop()]
                
                if stack:
                    cur_width = i-stack[-1]-1
                else:
                    cur_width = i
                    
                max_rect = max(max_rect, cur_height*cur_width)
                
            stack.append(i)
            
        return max_rect
