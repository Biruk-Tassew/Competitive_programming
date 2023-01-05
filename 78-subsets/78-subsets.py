class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        self.backtrack(0, [], nums)
            
        return self.res
    
    def backtrack(self, st_pt, cur_set, nums):
        self.res.append(cur_set[:])
        
        for i in range(st_pt, len(nums)):
            cur_set.append(nums[i])
            
            self.backtrack(i+1, cur_set, nums)
            
            cur_set.pop()