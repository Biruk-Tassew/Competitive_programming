# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    
    def dfs(self, node):
        if not node:
            return 
        self.count += 1
        self.dfs(node.left)
        self.dfs(node.right)
        