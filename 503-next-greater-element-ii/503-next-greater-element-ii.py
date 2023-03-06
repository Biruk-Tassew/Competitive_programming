class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        ans = [-1]*len(nums)
        flag = 0
        
        idx = 0
        while True:
            while stack and nums[stack[-1]] < nums[idx]:
                ans[stack.pop()] = nums[idx]
            
            if stack and nums[idx] == nums[stack[0]] and flag:
                break
            stack.append(idx)
            idx += 1
            if idx == len(nums):
                idx = 0
                flag = 1
                
        return ans