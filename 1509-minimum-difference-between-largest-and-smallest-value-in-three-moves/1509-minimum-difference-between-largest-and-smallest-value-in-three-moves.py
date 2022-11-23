class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        min_diff = float('inf')
        
        # change the three biggest elements
        min_diff = min(min_diff, nums[-4]-nums[0])
        
        # change the three smallest elemnts
        min_diff = min(min_diff, nums[-1]-nums[3])
        
        # change the the two smalles and 1 biggest element
        min_diff = min(min_diff, nums[-2]-nums[2])
        
        # change 1 smallest and 2 biggest elements
        min_diff = min(min_diff, nums[-3]-nums[1])
        
        return min_diff