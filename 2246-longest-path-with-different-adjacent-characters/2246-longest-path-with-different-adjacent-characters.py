class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.s = s
        self.graph = defaultdict(list)
        for i in range(1, len(parent)):
            self.graph[parent[i]].append(i)
        self.max_len = 1
        self.dfs(0)
        return self.max_len
    
    def dfs(self, node):
        if not node in self.graph:
            return 1
        
        left = right = 0
        for i in self.graph[node]:
            temp = self.dfs(i)
            if self.s[node] != self.s[i]:
    
                if temp > left:
                    left, right = temp, left
                else:
                    right = max(right, temp)
            
        self.max_len = max(self.max_len, left+right+1)
        return max(left, right)+1