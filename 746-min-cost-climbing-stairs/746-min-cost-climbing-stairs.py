class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        return self.solve(0)
    
    
    @cache
    def solve(self, cur_idx):
        if cur_idx >= len(self.cost)-1:
            return 0
        
        one_step = self.cost[cur_idx]+self.solve(cur_idx+1)
        two_steps = self.cost[cur_idx+1]+self.solve(cur_idx+2)
        return min(one_step, two_steps)
        
        