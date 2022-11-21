class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 0
        right = min(time)*totalTrips
        
        while left < right:
            mid = (left+right)//2
            cur_trips = sum(mid//t for t in time)
            
            if cur_trips < totalTrips:
                left = mid + 1
            else:
                right = mid 
                
        return left