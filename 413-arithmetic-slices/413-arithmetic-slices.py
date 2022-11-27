class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        res = 0
        
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i]-nums[i-1]:
                dp[i] = dp[i-1]+1
            res += dp[i]
            
        return res
        