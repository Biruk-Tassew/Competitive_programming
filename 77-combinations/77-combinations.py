class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.soln = []
        self.solve(1, k, [])
        return self.soln
        
    def solve(self, num, k, comb):
        if not k:
            self.soln.append(comb.copy())
        
        else:
            for i in range(num, self.n+1):
                comb.append(i)
                self.solve(i+1, k-1, comb)
                comb.pop()
            
        