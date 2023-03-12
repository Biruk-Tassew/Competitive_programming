class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        cur_upper = 0
        cur_lowwer = 0
        count = 0
       
        for i in range(len(nums)):
            cur_upper = upper - nums[i]
            cur_lower = lower - nums[i]
            left = bisect.bisect_left(nums, cur_lower)
            right = bisect.bisect_right(nums, cur_upper)
           
            count += right-left
            if left <= i < right:
                count -= 1
           
        return count//2