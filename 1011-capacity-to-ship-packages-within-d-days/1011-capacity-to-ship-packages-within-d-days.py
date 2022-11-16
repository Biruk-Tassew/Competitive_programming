class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = sum(weights)+1
        self.weights = weights
        self.days = days
        
        while left < right:
            mid = (left+right)//2
            
            if self.shippable(mid):
                right = mid 
            else:
                left = mid + 1
                
        return left
        
    def shippable(self, min_weight):
        cur_left = min_weight
        days = 1
        
        for i in self.weights:
            if i > min_weight:
                return False
            
            cur_left -= i
            
            if cur_left < 0:
                cur_left = min_weight - i
                days += 1
                
        return self.days >= days