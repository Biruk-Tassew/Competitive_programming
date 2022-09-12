class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [0]*(len(prices)+1)
        return self.solve(prices, memo, len(prices)-1, 0)
    
    def solve(self, prices, memo, n, max_profit):
        if n < 0:
            return 0
        
        if memo[n]:
            return memo[n]
        
        cur_profit = max_profit + prices[n] - prices[n-1]
        
        max_profit = max(max_profit, self.solve(prices, memo, n-1, max(cur_profit, 0)))
        memo[n] = max_profit
        
        return max_profit
