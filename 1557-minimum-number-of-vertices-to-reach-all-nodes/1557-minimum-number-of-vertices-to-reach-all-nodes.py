class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        in_degree = defaultdict(lambda: 0)
        for edge in edges:
            in_degree[edge[1]] += 1
            
        res = []
        for i in range(0, n):
            if not in_degree[i]:
                res.append(i)
                
        return res