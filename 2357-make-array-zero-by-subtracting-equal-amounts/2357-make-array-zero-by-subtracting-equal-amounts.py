class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        count = 0
        while sum(nums):
            min_num = float('inf')
            
            for i in nums:
                if i and i < min_num:
                    min_num = i
            
            for i in range(len(nums)):
                if nums[i]:
                    nums[i] -= min_num
            count += 1
                    
        return count