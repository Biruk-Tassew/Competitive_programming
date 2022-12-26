class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if not nums[0]:
            return False
        cur_jumps = nums[0]
        
        for i in range(1, len(nums)-1):
            cur_jumps -= 1
            
            cur_jumps = max(cur_jumps, nums[i])
            if not cur_jumps:
                return False
            
        return True