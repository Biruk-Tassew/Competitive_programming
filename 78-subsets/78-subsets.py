class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        for i in range(len(nums)+1):
            self.solve(0, [], nums, i)
            
        return self.res
        
    def solve(self, cur_start, cur_set, nums, cur_last):
        if cur_last == len(cur_set):
            self.res.append(cur_set.copy())
            return
            
        for i in range(cur_start, len(nums)):
            cur_set.append(nums[i])
            
            self.solve(i+1, cur_set, nums, cur_last)
            
            cur_set.pop()