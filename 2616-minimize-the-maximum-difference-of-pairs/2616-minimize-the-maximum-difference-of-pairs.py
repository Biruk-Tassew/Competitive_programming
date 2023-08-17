class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]
        
        while left < right:
            mid = left + (right-left)//2
            
            if self.cnt_no_pairs(mid, nums) >= p:
                right = mid
            else:
                left = mid + 1
                
        return left
        
    def cnt_no_pairs(self, max_diff, nums):
        cur_cnt = 0
        idx = 0
        while idx < len(nums)-1:
            if abs(nums[idx]-nums[idx+1]) <= max_diff:
                idx += 1
                cur_cnt += 1
                
            idx += 1
            
        return cur_cnt
            
            