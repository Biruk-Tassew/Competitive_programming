class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sum_ = sum(nums)
        start_sum = 0
        
        for i in range(len(nums)):
            sum_ -= nums[i]
            
            if sum_ == start_sum:
                return i
            
            start_sum += nums[i]
            
        return -1
