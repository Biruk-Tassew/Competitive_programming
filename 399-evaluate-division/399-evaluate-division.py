class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))
            
        ans = [-1.0]*len(queries)
        for i in range(len(queries)):
            if queries[i][0] not in graph or queries[i][1] not in graph:
                continue
                
            seen = set()
            que = deque([(queries[i][0], 1)])
            while que:
                node, value = que.popleft()
                
                if node == queries[i][-1]:
                    ans[i] = value
                    break
                for child in graph[node]:
                    
                    if child not in seen:
                        que.append((child[0], child[1]*value))
                        seen.add(child)
                        
        return ans