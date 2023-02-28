class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = defaultdict(lambda: -1)
        return self.dfs(len(nums)-1, nums)
    
    def dfs(self, cur_idx, nums):
        if cur_idx < 0:
            return 0
        if cur_idx == 1:
            return max(nums[1], nums[0])
        
        if self.memo[cur_idx] != -1:
            return self.memo[cur_idx]
        
        self.memo[cur_idx] = max(self.dfs(cur_idx-1, nums), self.dfs(cur_idx-2, nums)+nums[cur_idx])
        return self.memo[cur_idx]