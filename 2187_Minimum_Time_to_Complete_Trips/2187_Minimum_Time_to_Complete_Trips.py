class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
       
        left = 0
        right = max(time)*totalTrips
        
        while left <= right:
            mid = (left+right)//2
            middle_trip = sum(mid//t for t in time)
            
            if middle_trip < totalTrips:
                left = mid + 1
            elif middle_trip >= totalTrips:
                right = mid - 1
            
        return left
