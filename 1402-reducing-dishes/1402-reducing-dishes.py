class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = defaultdict(lambda: "*")
        return self.dfs(0, 1, satisfaction, memo)
    def dfs(self, cur_idx, cur_dishes, sat, memo):
        if cur_idx == len(sat):
            return 0
        
        if memo[(cur_idx, cur_dishes)] != "*":
            return memo[(cur_idx, cur_dishes)] 
        
        make_dish = sat[cur_idx]*cur_dishes + self.dfs(cur_idx+1, cur_dishes+1, sat, memo)
        leave_dish =  self.dfs(cur_idx+1, cur_dishes, sat, memo)
        
        memo[(cur_idx, cur_dishes)] = max(0, make_dish, leave_dish)
        return memo[(cur_idx, cur_dishes)] 