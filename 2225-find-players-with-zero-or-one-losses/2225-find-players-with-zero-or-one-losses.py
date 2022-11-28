class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        nodes = set()
        in_degree = defaultdict(int)
        for match in matches:
            in_degree[match[1]] += 1
            nodes.add(match[0])
            nodes.add(match[1])
            
        ans = [[], []]
        for node in nodes:
            if in_degree[node]==1:
                ans[1].append(node)
            elif not in_degree[node]:
                ans[0].append(node)
                
                
        return [sorted(ans[0]), sorted(ans[1])]