class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        self.memo = defaultdict(lambda: "")
        return self.dfs(nums, 0, True)
    
    def dfs(self, nums, cur_idx, isEven):
        if cur_idx == len(nums):
            return 0
        
        if self.memo[(cur_idx, isEven)]:
            return self.memo[(cur_idx, isEven)]
        
        num = nums[cur_idx] if isEven else -nums[cur_idx]
        
        take = num + self.dfs(nums, cur_idx+1, not isEven)
        not_take = self.dfs(nums, cur_idx+1, isEven)
        
        self.memo[(cur_idx, isEven)] = max(take, not_take)
        return self.memo[(cur_idx, isEven)]