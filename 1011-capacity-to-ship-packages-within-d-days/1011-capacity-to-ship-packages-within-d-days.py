class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)
        self.weights = weights
        self.days = days
        
        while left < right:
            
            mid = (right+left)//2
            
            if self.shipable(mid):
                right = mid
            else:
                left = mid + 1
                
        return left 
    
    def shipable(self, ship_capacity):
        cur_cap = ship_capacity
        days = 0
        idx = 0
        
        while idx < len(self.weights):
            while idx < len(self.weights) and cur_cap - self.weights[idx] >= 0:
                cur_cap -= self.weights[idx]
                idx += 1
            
            days += 1
            if self.days < days:
                return False
            cur_cap = ship_capacity
        
        
        if self.days < days:
            return False
        return True