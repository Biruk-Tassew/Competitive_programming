class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.graph = defaultdict(list)
        
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
            
        return max(self.dfs(0, -1)-2, 0)
        
    def dfs(self, node, parent):
        
        res = 0
        
        for i in self.graph[node]:
            if i != parent:
                res += self.dfs(i, node)
                
        if res or self.hasApple[node]:
            res += 2
            
        return res