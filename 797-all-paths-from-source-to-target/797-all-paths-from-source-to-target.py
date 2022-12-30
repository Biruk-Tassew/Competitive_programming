class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.graph = graph
        self.dfs([], 0, 0, len(graph)-1)
        return self.paths
    
    def dfs(self, path, node, start, end):
        path.append(node)
        
        if node == end:
            self.paths.append(path.copy())
            return 
        
        for i in self.graph[node]:
            self.dfs(path, i, node, end)
            path.pop()