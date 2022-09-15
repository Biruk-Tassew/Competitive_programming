class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pos = -prices[0]
        cool = -prices[0]
        profit = 0
        
        for i in range(len(prices)):
            pos = max(pos, profit-prices[i])
            profit = max(profit, cool)
            cool = pos + prices[i]
            
        return max(profit, cool)
