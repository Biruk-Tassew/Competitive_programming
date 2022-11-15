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
        self.prev = None
        self.node_one = None
        self.node_two = None
        self.dfs(root)
        
        if self.node_one and self.node_two:
            self.node_one.val, self.node_two.val = self.node_two.val, self.node_one.val
        
    def dfs(self, node):
        if not node:
            return 
        
        self.dfs(node.left)
        
        if self.prev and self.prev.val > node.val:
            if not self.node_one:
                self.node_one = self.prev
            self.node_two = node
                
        self.prev = node
        
        self.dfs(node.right)