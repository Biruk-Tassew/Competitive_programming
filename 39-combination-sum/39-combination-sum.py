class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.cands = candidates
        self.solve(0, [], 0, target)
    
        return self.res
        
    def solve(self, st_idx, cur_nums, cur_sum, target):
        if cur_sum >= target:
            if cur_sum == target:
                self.res.append(sorted(cur_nums[:]))
            return 
        
        for i in range(st_idx, len(self.cands)):
            cur_nums.append(self.cands[i])
            cur_sum += self.cands[i]
            
            self.solve(i, cur_nums, cur_sum, target)
            
            cur_nums.pop()
            cur_sum -= self.cands[i]