class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre_sum = [0]
        for i in range(1, len(nums)+1):
            pre_sum.append(pre_sum[i-1]+nums[i-1])
            
        ans_idx = 0    
        min_diff = float('inf')
        for i in range(1, len(nums)):
            cur_diff = abs((pre_sum[i]//i) - (pre_sum[-1]-pre_sum[i])//(len(pre_sum)-1-i))
            
            if cur_diff < min_diff:
                min_diff = cur_diff
                ans_idx = i
                
        last_diff = pre_sum[-1]//(len(pre_sum)-1)
        if last_diff < min_diff:
            return len(pre_sum)-2
                
        return ans_idx-1