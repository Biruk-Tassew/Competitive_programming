#Bottom-up
class Solution:
    def rob(self, nums: List[int]) -> int:
      dp = [0]*(len(nums)+1)
      dp[1] = nums[0]
      
      for i in range(2, len(nums)+1):
        dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        
       return dp[-1]
    
#Top-down
class Solution:
    def rob(self, nums: List[int]) -> int:
      
    def solve(self, nums, memo, n):
      if n < 0:
        return 0
      
      if memo[n] != -1:
        return memo[n]
      
      memo[n] = max(self.solve(nums, memo, n-2) + nums[n] + self.solve(nums, memo, n-1))
      return memo[n]
