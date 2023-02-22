class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(lambda: 0)
        ans = 0
        for t in time:
            t %= 60
            
            if (60-t) in count:
                ans += count[60-t]
            elif not t:
                ans += count[t]
                
            count[t] += 1
            
        return ans
                
                