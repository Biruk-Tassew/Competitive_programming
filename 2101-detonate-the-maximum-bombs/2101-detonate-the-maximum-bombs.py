class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                x, y, r = bombs[i]
                x_2, y_2, r_2 = bombs[j]
                if r ** 2 >= (x - x_2) ** 2 + (y - y_2) ** 2 and i != j:
                    graph[i].append(j)
      
        max_len = 0
        
        for i in range(len(bombs)):
            visited = set()
            max_len = max(max_len, self.dfs(i, visited, graph))
              
        return max_len
    
    def dfs(self, node, visited, graph):
        
        visited.add(node)
        
        for i in graph[node]:
            if i not in visited:
                self.dfs(i, visited, graph)
                
        return len(visited)