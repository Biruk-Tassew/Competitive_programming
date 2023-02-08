class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        for i in range(len(routes)):
            for route in routes[i]:
                graph[route].append(i)
                
        seen = set()
        que = deque([source])
        level = 1
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                
                for i in graph[node]:
                    if i not in seen:
                        seen.add(i)
                        
                        for child in routes[i]:
                            if child == target:
                                return level
                            que.append(child)
            level += 1
            
        return -1