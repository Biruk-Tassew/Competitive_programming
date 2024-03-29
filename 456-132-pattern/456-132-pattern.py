class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        comp = float('-inf')
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < comp:
                return True
            
            while stack and stack[-1] < nums[i]:
                comp = stack.pop()
            stack.append(nums[i])
        return False