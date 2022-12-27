class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [capacity[i]-rocks[i] for i in range(len(rocks))]
        diff.sort()
        count = 0
        
        for i in diff:
            if not i:
                count += 1
            elif i <= additionalRocks:
                count += 1
                additionalRocks -= i
                
        return count
                