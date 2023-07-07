class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.parents = {i: i for i in set(s1+s2+baseStr)}
        
        for i in range(len(s2)):
            self.union(s1[i], s2[i])
              
        ans = ""
        for i in baseStr:
            ans += self.find(i)
            
        return ans
    def union(self, parent, child):
        par_rep = self.find(parent)
        ch_rep = self.find(child)
        
        self.parents[max(ch_rep, par_rep)] = min(ch_rep, par_rep)
        
    def find(self, child):
        if self.parents[child] == child:
            return child
        
        self.parents[child] = self.find(self.parents[child])
        return self.parents[child]