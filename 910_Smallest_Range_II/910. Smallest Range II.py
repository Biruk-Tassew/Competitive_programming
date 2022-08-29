class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = nums[0] + k
        right = nums[-1] - k
        score = nums[-1] - nums[0]
        
        for i, j in zip(nums, nums[1:]):
            less = min(left, j-k)
            greater = max(right, i+k)
            score = min(score, greater-less)
            
            
        return score
