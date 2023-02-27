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
        if sideLen == 1:
            return Node(self.grid[row][col], True)
        
        topLeft = self.buildGraph(row, col, sideLen//2)
        topRight = self.buildGraph(row, col+sideLen//2, sideLen//2)
        bottomLeft = self.buildGraph(row+sideLen//2, col, sideLen//2)
        bottomRight = self.buildGraph(row+sideLen//2, col+sideLen//2, sideLen//2)
            
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return Node(topLeft.val, True)
    
        return Node(topLeft.val, False, topLeft, topRight, bottomLeft, bottomRight)