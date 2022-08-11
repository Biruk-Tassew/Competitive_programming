# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        node, depth = self.dfs(root)
        return node
        
    def dfs(self, node):
        if not node:
            return (node, 0)
        
        left, left_depth = self.dfs(node.left)
        right, right_depth = self.dfs(node.right)
        
        if left_depth > right_depth:
            return (left, left_depth+1)
        elif left_depth < right_depth:
            return (right, right_depth+1)
        return node, left_depth+1
