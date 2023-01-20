class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = []
        self.backtrack(0, [])
        
        return self.res
    
    def backtrack(self, st_idx, cur_list):
        if st_idx == len(self.nums):
            if len(cur_list) > 1 and cur_list not in self.res:
                self.res.append(cur_list.copy())
            return 
        
        if len(cur_list) > 1 and cur_list not in self.res:
            self.res.append(cur_list.copy())
        
        for i in range(st_idx, len(self.nums)):
            if not cur_list or self.nums[i] >= cur_list[-1]:
                cur_list.append(self.nums[i])
                
                self.backtrack(i+1, cur_list)
                
                cur_list.pop()