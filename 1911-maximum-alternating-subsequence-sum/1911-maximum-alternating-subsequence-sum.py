class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        self.nums = nums
        return self.dfs(0, True)
    
    @cache
    def dfs(self, cur_idx, isEven):
        if cur_idx == len(self.nums):
            return 0
            
        num = self.nums[cur_idx] if isEven else -self.nums[cur_idx]
        
        take = num + self.dfs(cur_idx+1, not isEven)
        not_take = self.dfs(cur_idx+1, isEven)
        
        return max(take, not_take)