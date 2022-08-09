class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        provinces = 0
        
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] and col not in self.visited:
                    self.visited.add(col)
                    self.dfs(col, isConnected)
                    provinces += 1
                    
        return provinces 
                    
    def dfs(self, row, isConnected):
        for col in range(len(isConnected[row])):
            if isConnected[row][col] and col not in self.visited:
                    self.visited.add(col)
                    self.dfs(col, isConnected)
        
