class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = defaultdict(lambda : "W")
        self.n_graph = defaultdict(list)
        for i in range(len(graph)):
            self.n_graph[i] = graph[i]
        res = []
        for i in range(len(graph)):
            if not self.dfs(i, colors):
                res.append(i)
                
        return res
    def dfs(self, node, colors):
        
        colors[node] = "G"
        for i in self.n_graph[node]:
            if colors[i] == "G":
                return True
            
            if colors[i] == "W" and self.dfs(i, colors):
                return True
            
        colors[node] = "B"
        return False
    
    