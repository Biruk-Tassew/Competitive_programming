class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.memo = {0:[nums[0], nums[0]]}
        self.nums = nums
        self.solve(len(nums)-1)
        
        return max(self.memo[i][0] for i in self.memo)
    
    def solve(self, cur_idx):
        if cur_idx in self.memo:
            return self.memo[cur_idx]
        
        temp = self.solve(cur_idx-1)
        self.memo[cur_idx] = [max(self.nums[cur_idx], self.nums[cur_idx]*temp[0], self.nums[cur_idx]*temp[1]), min(self.nums[cur_idx], self.nums[cur_idx]*temp[0], self.nums[cur_idx]*temp[1])]
        
        return self.memo[cur_idx]