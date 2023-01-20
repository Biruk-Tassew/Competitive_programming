class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.res = set()
        self.backtrack(0, [])
        
        return self.res
    
    def backtrack(self, cur_idx, cur_list):
        if cur_idx == len(self.nums):
            if len(cur_list) > 1:
                self.res.add(tuple(cur_list))
            return 
        
        
        if not cur_list or self.nums[cur_idx] >= cur_list[-1]:
            cur_list.append(self.nums[cur_idx])
            
            self.backtrack(cur_idx+1, cur_list)
            
            cur_list.pop()
            
        self.backtrack(cur_idx+1, cur_list)