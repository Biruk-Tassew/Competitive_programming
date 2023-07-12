class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parents = {}
        
        for i in equations:
            if i[1] == "=":
                self.union(i[0], i[-1])
                
                
        for i in equations:
            if i[1] == "!" and self.find(i[0]) == self.find(i[-1]):
                return False
            
        return True
                
        
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
        
    def find(self, child):
        self.parents.setdefault(child, child)
        if self.parents[child] == child:
            return child
        return self.find(self.parents[child])