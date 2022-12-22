class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(list)
        self.n = n
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
            
        self.count = [1]*n
        self.ans = [0]*n
        
        self.dfs(0, None)
        self.second_dfs(0, None)
        return self.ans
        
    def dfs(self, node, parent):
        for i in self.graph[node]:
            if i != parent:
                self.dfs(i, node)
                self.count[node] += self.count[i]
                self.ans[node] += self.ans[i] + self.count[i]
    
    def second_dfs(self, node, parent):
        for i in self.graph[node]:
            if i != parent:
                self.ans[i] = self.ans[node] - self.count[i] + self.n - self.count[i]
                self.second_dfs(i, node)