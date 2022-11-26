class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        start, end, profit = zip(*sorted(zip(startTime, endTime, profit)))
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(len(endTime))}
        dp = [0 for _ in range(len(endTime)+1)]
        
        for i in range(len(endTime)-1, -1, -1):
            dp[i] = max(dp[i+1], profit[i] + dp[jump[i]])
            
        return dp[0]