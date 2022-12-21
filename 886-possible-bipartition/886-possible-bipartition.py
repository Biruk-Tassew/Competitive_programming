class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        
        self.graph = defaultdict(list)
        
        for i in dislikes:
            self.graph[i[0]].append(i[1])
            self.graph[i[1]].append(i[0])
            
        self.color = defaultdict(lambda: -1)
        for i in range(1, n+1):
            if self.color[i] == -1:
                if not self.bfs(i):
                    return False
        return True
        
        
    def bfs(self, node):
        que = deque([node])
        self.color[node] = 0
        
        while que:
            node = que.popleft()
            
            for i in self.graph[node]:
                
                if self.color[i] == self.color[node]:
                    return False
                
                if self.color[i] == -1:
                    self.color[i] = 1 - self.color[node]
                    
                    que.append(i)
        return True