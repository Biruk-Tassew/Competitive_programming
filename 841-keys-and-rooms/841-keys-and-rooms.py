class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set([0])
        self.rooms = rooms
        self.dfs(0)
        return len(self.visited) == len(rooms)
    
    def dfs(self, node):
        self.visited.add(node)
        
        for i in self.rooms[node]:
            if i not in self.visited:
                self.dfs(i)