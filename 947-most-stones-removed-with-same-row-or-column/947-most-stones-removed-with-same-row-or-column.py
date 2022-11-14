class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        self.parents = {}
        for i, j in stones:
            self.parents.setdefault(i, i)
            self.parents.setdefault(~j, ~j)
            self.union(i, ~j)
        return len(stones) - len(set([self.find(x) for x in self.parents]))
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

    
    