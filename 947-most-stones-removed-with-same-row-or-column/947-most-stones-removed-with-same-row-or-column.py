class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parents = {}
        
        for row, col in stones:
            self.parents.setdefault(row, row)
            self.parents.setdefault(str(col)+"c", str(col)+"c")
            self.union(row, str(col)+"c")
            
        
        return len(stones) - len(set([self.find(child) for child in self.parents]))
    
    def find(self, child):
        if child != self.parents[child]:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]
        
    def union(self, ch_one, ch_two):
        self.parents[self.find(ch_one)] = self.find(ch_two)
        
        
        
#     o x
#     x o