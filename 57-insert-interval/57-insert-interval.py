class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        s, e = newInterval
        li, ri = self.search(intervals, s), self.search(intervals, e)
        l = intervals[:li + int(li < len(intervals) and intervals[li][1] < s)]
        r = intervals[ri + int(ri >= len(intervals) or intervals[ri][0] <= e):]
        if len(l) + len(r) != len(intervals):
            s = min(s, intervals[len(l)][0])
            e = max(e, intervals[-len(r)-1][1])
        return l + [[s, e]] + r

    def search(self, intervals, num):
        left = 0
        right = len(intervals)
        
        while left < right:
            mid = (left+right)//2
            
            if intervals[mid][0] > num:
                right = mid
            elif intervals[mid][1] < num:
                left = mid + 1
            else:
                return mid
            
        return mid
                
            
                
            