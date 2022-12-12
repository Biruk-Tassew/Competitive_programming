class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left+right)//2
            
            cur_hr = sum(ceil(p/mid) for p in piles)
            
            if cur_hr <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left