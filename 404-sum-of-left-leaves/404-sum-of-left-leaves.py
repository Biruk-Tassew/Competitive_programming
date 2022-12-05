# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, None)
        return self.res
    def dfs(self, node, parent):
        if not node:
            return 
        
        self.dfs(node.left, node)
        if parent and parent.left == node and not node.left and not node.right:
            self.res += node.val
        self.dfs(node.right, node)