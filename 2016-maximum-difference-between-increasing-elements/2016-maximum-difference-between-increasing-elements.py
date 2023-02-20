class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        cur_min = nums[0]
        max_num = -1
        
        for i in range(1, len(nums)):
            
            max_num = max(max_num, nums[i] - cur_min)
            cur_min = min(cur_min, nums[i])
            
            
        if max_num:
            return max_num
        return -1
            