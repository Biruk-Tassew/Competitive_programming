class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(nums[i]+pre_sum[-1])
        max_av = float('-inf')
        
        for i in range(k, len(pre_sum)):
            max_av = max((pre_sum[i]-pre_sum[i-k])/k, max_av) 
        return max_av