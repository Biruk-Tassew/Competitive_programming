class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parent = {}
        for i in range(len(accounts)):
            self.parent[i] = i
        
                
        cur_par = 0
        owner = defaultdict(list)
        for account in accounts:
            for email in account[1:]:
                owner[email].append(cur_par)
            cur_par += 1  
            
        for acc in owner:
            for par in owner[acc][1:]:
                self.union(owner[acc][0], par)
                
                
        res = defaultdict(set)
        for i in range(len(accounts)):
            res[self.find(i)].update(accounts[i][1:])
          
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
        
    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        
        self.parent[x_par] = y_par