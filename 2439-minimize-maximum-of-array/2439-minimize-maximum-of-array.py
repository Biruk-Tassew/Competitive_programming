class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        cur_sum = 0
        cur_max = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur_max = max(cur_max, ceil(cur_sum/(i+1)))
            
        return cur_max