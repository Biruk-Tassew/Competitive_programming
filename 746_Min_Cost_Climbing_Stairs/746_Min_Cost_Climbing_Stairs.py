class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0]*len(cost)
        return min(self.solve(cost, len(cost)-1, memo), self.solve(cost, len(cost)-2, memo))
    
    def solve(self, cost, n, memo):
        if n < 0:
            return 
        if n < 2:
            return cost[n]
        
        if memo[n]:
            return memo[n]
        
        memo[n] = cost[n] + min(self.solve(cost, n-1, memo), self.solve(cost, n-2, memo))
        return memo[n]
