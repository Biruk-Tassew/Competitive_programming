class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.days = days
        
        left = 0
        right = sum(self.weights)
        
        while left < right:
            mid = (left + right) // 2
            if self.shippable(mid):
                right = mid 
            else:
                left = mid + 1

        return left
    
    def shippable(self, capacity):
        left = capacity 
        day = 1
        for i in self.weights:
            if i > capacity:
                return False
            
            left -= i
            if left < 0:
                day += 1
                left = capacity - i
                
        return day <= self.days
