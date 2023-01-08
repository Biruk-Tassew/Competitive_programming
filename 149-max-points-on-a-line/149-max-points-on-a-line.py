class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        max_overall = 0
        
        for i in points:
            angle_cnt = defaultdict(lambda: 1)
            max_count = 2
            for j in points:
                if i == j:
                    continue
                
                angle_cnt[atan2(j[1]-i[1], j[0]-i[0])] += 1
                max_count = max(max_count, angle_cnt[atan2(j[1]-i[1], j[0]-i[0])] )
            
            max_overall = max(max_overall, max_count)
        
        return max_overall