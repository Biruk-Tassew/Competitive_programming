class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_one = (ax2-ax1)*(ay2-ay1)
        area_two = (bx2-bx1)*(by2-by1)
        
        w_over_lap = min(ax2, bx2) - max(ax1, bx1)
        h_over_lap = min(by2, ay2) - max(ay1, by1)
        
        if w_over_lap >=0 and h_over_lap >= 0:
            return (area_one+area_two)-(w_over_lap*h_over_lap)
        
        return (area_one+area_two)