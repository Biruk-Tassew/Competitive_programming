class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        for i in range(len(nums)+1):
            self.backtrack(0, [], i, nums)
            
        return self.res
    
    def backtrack(self, st_pt, cur_set, en_pt, nums):
        if len(cur_set) == en_pt:
            self.res.append(cur_set[:])
            return 
        
        for i in range(st_pt, len(nums)):
            cur_set.append(nums[i])
            
            self.backtrack(i+1, cur_set, en_pt, nums)
            
            cur_set.pop()