"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, cur_depth = stack.pop()
            if node:
                depth = max(depth, cur_depth)
                for child in node.children:
                    stack.append((child, cur_depth+1))
                    
        return depth
