class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for edge in relations:
            graph[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
            
       
        heap = []
        for i in range(1, n+1):
            if not in_degree[i]:
                heappush(heap, (time[i-1], i))
                
        total_time = 0
        while heap:
            total_time, node = heappop(heap)
            for child in graph[node]:
                
                in_degree[child] -= 1
                
                if not in_degree[child]:       
                    heappush(heap, (time[child-1]+total_time, child))
                    
           
            
        return total_time