class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        cur_list = []
        total_list = []
        
        self.backtrack(0, cur_list, total_list, nums)
        
        return max(Counter(total_list).values())
    
    def backtrack(self, cur_idx, cur_list, total_list, nums):
        if cur_idx >= len(nums):
            cur_or = 0
            for i in cur_list:
                cur_or |= i
            total_list.append(cur_or)
            return
        
        cur_list.append(nums[cur_idx])
        
        self.backtrack(cur_idx+1, cur_list, total_list, nums)
        
        cur_list.pop()
        
        self.backtrack(cur_idx+1, cur_list, total_list, nums)