class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        last_seen = {}
        for i in range(len(nums)):
            last_seen[nums[i]] = i
        
        min_len = float('inf')
        for i in count:
            if count[i] == max_freq:
                min_len = min(min_len, last_seen[i] - nums.index(i)+1)
                
        return min_len
                
        