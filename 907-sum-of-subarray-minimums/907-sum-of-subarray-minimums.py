class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        min_sum = 0
        stack = []
        
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]] >= arr[i]):
                
                cur_min_idx = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                
                win_width = (cur_min_idx-left)*(right-cur_min_idx)
                min_sum += win_width*arr[cur_min_idx]
                
            stack.append(i)
            
        return min_sum%(10**9 + 7)