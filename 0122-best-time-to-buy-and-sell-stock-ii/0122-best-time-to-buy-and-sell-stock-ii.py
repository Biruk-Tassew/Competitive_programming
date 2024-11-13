class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min_price = float('inf')
        profit = 0
        
        for price in prices:
            if price < cur_min_price:
                cur_min_price = price
            elif price > cur_min_price:
                profit += price - cur_min_price
                cur_min_price = price
                
        return profit