class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        
        return self.solve(0, 0)
    
    @lru_cache  
    def solve(self, cur_idx, sell):
        if cur_idx >= len(self.prices):
            return 0
        
        temp = 0  
        if not sell:
            temp = max(self.solve(cur_idx+1, sell-1)-self.prices[cur_idx], self.solve(cur_idx+1, sell))
        else:
            temp = max(self.solve(cur_idx+2, sell+1)+self.prices[cur_idx], self.solve(cur_idx+1, sell))
        
        return temp