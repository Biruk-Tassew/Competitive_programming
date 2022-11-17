# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.dfs(root, p, q)
        return self.res
    
    def dfs(self, node, p, q):
        if not node:
            return False
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        
        mid = node == p or node == q 
        
        if mid + left + right >= 2:
            self.res = node
            
        return mid or left or right