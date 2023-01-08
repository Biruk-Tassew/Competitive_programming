class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        self.stones_set = set(stones)
        self.stones = stones
        self.memo = defaultdict(lambda: -1)
        return self.jump(1, 1)
    
  
    def jump(self, cur_jump, cur_loc):
        if cur_loc == self.stones[-1]:
            return True
        
        if self.memo[(cur_jump, cur_loc)] != -1:
            return self.memo[(cur_jump, cur_loc)]
        
        can_reach = False
        
        for jump in [cur_jump-1, cur_jump, cur_jump+1]:
            if jump > 0 and cur_loc+jump in self.stones_set:
                can_reach = can_reach or self.jump(jump, cur_loc + jump)
            
        
        self.memo[(cur_jump, cur_loc)] = can_reach
        return self.memo[(cur_jump, cur_loc)]