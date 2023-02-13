class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (not(low & 1)):
            low += 1
    
        
        if low > high: 
            return 0 
        return (high - low) // 2 + 1