class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        last_seen = {}
        for i in range(len(nums)):
            if nums[i] not in last_seen:
                last_seen[nums[i]] = [i, i]
            else:
                last_seen[nums[i]][1] = i
        
        min_len = float('inf')
        for i in count:
            if count[i] == max_freq:
                min_len = min(min_len, last_seen[i][1]-last_seen[i][0]+1)
                
        return min_len
                
        