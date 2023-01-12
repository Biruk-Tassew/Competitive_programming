class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        label_count = defaultdict(lambda: 0)
        graph = defaultdict(list)
        answer = {}
        visited = set()
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        self.dfs(0, visited, labels, graph, answer)
        best = []
        for i in range(len(answer)):
            best.append(answer[i])
        return best
            
    def dfs(self, node, visited, labels, graph, answer):
        
        visited.add(node)
        current = None
        for child in graph[node]:
            if child not in visited:
                temp = self.dfs(child, visited, labels, graph, answer)
                if not current:
                    current = temp
                else:
                    for i in range(26):
                        current[i] += temp[i]
        if not current:
            current = [0] * 26
        idx = ord(labels[node]) - ord('a')
        current[idx] += 1
        answer[node] = current[idx]
        
        return current
        
                
        
        
        