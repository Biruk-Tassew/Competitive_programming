class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
            
        que = deque()
        for i in range(0, numCourses):
            if not in_degree[i]:
                que.append(i)
                
        pres = defaultdict(set)
        while que:
            node = que.popleft()
            
            for child in graph[node]:
                pres[child].add(node)
                pres[child].update(pres[node])
                in_degree[child] -= 1
                
                if not in_degree[child]:
                    que.append(child)    
        ans = [query[0] in pres[query[1]] for query in queries]
        return ans