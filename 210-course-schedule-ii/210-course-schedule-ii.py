class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1
            
        que = deque()
        for node in range(numCourses):
            if not in_degree[node]:
                que.append(node)
                
        path = []
        while que:
            node = que.popleft()
            path.append(node)
            for child in graph[node]:
                in_degree[child] -= 1
                if not in_degree[child]:
                    que.append(child)
                    
        if len(path) == numCourses:
            return path
        return []