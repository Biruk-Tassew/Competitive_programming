# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('inf'), float('-inf'))
        
    def dfs(self, root, max_val, min_val):
        if not root:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            return False
        
        return self.dfs(root.left, min(root.val, max_val), min_val) and self.dfs(root.right, max_val, max(root.val, min_val))
        
        