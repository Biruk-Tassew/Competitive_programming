class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        
        non_weak_arthms = 0
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] += dp[j][diff]+1
                non_weak_arthms += dp[j][diff]
          
        return non_weak_arthms
                