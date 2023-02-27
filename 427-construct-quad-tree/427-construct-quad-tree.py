"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        return self.buildGraph(0, 0, len(grid))
    def buildGraph(self, row, col, sideLen):
        check_all = True
        prev_val = self.grid[row][col]
        for r in range(row, row+sideLen):
            for c in range(col, col+sideLen):
                if self.grid[r][c] != prev_val:
                    check_all = False
                    break
            if not check_all:
                break
        if check_all:
            return Node(prev_val, True)
        
        root = Node(prev_val, False)
        
        root.topLeft = self.buildGraph(row, col, sideLen//2)
        root.topRight = self.buildGraph(row, col+sideLen//2, sideLen//2)
        root.bottomLeft = self.buildGraph(row+sideLen//2, col, sideLen//2)
        root.bottomRight = self.buildGraph(row+sideLen//2, col+sideLen//2, sideLen//2)
            
        return root
        