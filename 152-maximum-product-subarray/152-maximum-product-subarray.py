class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[nums[0], nums[0]]]
        max_overall = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dp[i-1][0], dp[i-1][1] = dp[i-1][1], dp[i-1][0]
                
            dp.append([max(nums[i], dp[i-1][0]*nums[i]), min(nums[i], dp[i-1][1]*nums[i])])
            max_overall = max(max_overall, dp[i][0])
        
        return max_overall