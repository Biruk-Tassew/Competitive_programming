# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)
    
    def dfs(self, node, cur_min, cur_max):
        if not node:
            return abs(cur_min-cur_max)
        
        cur_min = min(cur_min, node.val)
        cur_max = max(cur_max, node.val)
        left = self.dfs(node.left, cur_min, cur_max)
        right = self.dfs(node.right, cur_min, cur_max)
        
        return max(left, right)
        
        