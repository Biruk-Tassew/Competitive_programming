class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = defaultdict(list)
        for i in edges:
            self.graph[i[0]].append(i[1])
            self.graph[i[1]].append(i[0])
            
        self.visited = set([source])
        self.destination = destination 
        if self.dfs(source):
            return True
        return False
    
    def dfs(self, node):
        if node == self.destination:
            return True
        
        for i in self.graph[node]:
            if i not in self.visited:
                self.visited.add(i)
                if self.dfs(i):
                    return True