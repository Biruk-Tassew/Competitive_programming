class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        max_len = 0
        dp = defaultdict(lambda: 0)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                dp[(j, nums[j]-nums[i])] = dp[(i, nums[j]-nums[i])] + 1
                max_len = max(max_len, dp[(j, nums[j]-nums[i])] + 1)
                
        return max_len
                