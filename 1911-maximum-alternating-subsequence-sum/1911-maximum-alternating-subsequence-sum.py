class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        even_sums = [0]*(len(nums)+1)
        odd_sums = [0]*(len(nums)+1)
        
        for i in range(1, len(even_sums)):
            even_sums[i] = max(odd_sums[i-1]-nums[i-1], even_sums[i-1])
            odd_sums[i] = max(even_sums[i-1]+nums[i-1], odd_sums[i-1])
            
        return odd_sums[-1]