class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        cur_sum = 0
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while left <= right and cur_sum >= target:
                min_len = min(min_len, right-left+1)
                cur_sum -= nums[left]
                left += 1
                
            
            
        if min_len == float('inf'):
            return 0
        return min_len