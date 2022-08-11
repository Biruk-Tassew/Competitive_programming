# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.left = None
        self.right = None
        self.prev = None
        
        self.dfs(root)
        if self.left and self.right:
            self.left.val, self.right.val = self.right.val, self.left.val
        
        
    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        
        if self.prev and self.prev.val > node.val:
            if not self.left:
                self.left = self.prev
            if self.left:
                self.right = node
                
        self.prev = node
        
        if node.right:
            self.dfs(node.right)
