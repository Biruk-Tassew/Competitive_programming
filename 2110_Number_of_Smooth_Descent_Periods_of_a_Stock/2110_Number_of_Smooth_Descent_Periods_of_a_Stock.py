class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        store = [1]*len(prices)
        
        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i-1]:
                store[i] += store[i-1]
                
        return sum(store)
