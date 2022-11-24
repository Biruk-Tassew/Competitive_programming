class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        cur_idx = 0
        stack = []
        
        while cur_idx < len(height):
            while stack and height[stack[-1]] < height[cur_idx]:
                stack_height = stack.pop()
                
                if not stack:
                    break
                    
                dis = cur_idx - stack[-1] - 1
                min_height = min(height[cur_idx], height[stack[-1]])-height[stack_height]
                
                res += (dis*min_height)
                
            stack.append(cur_idx)
            cur_idx += 1
            
        return res
                