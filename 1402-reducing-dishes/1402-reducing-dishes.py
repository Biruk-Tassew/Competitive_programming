class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        cur_sum = 0
        total = 0
        
        for i in range(len(satisfaction)):
            cur_sum += satisfaction[i]
            
            if cur_sum < 0:
                return total
            
            total += cur_sum
            
        return total
        