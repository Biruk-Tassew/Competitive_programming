class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        total = sum(nums)
        cur_sum = 0
        ans_idx = 0    
        min_diff = float('inf')
        for i in range(len(nums)):
            cur_sum += nums[i]
            left_avg = cur_sum//(i+1) 
            
            right_avg = total-cur_sum
            if i != len(nums)-1:
                right_avg //= (len(nums)-i-1)
                
            cur_diff = abs(right_avg-left_avg)
            if cur_diff < min_diff:
                min_diff = cur_diff
                ans_idx = i
                
                    
        return ans_idx