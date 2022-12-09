# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, root.val, root.val)
        return self.res
    
    def dfs(self, node, cur_min, cur_max):
        if not node:
            return 
        
        self.res = max(self.res, abs(cur_min-node.val), abs(cur_max-node.val))
        cur_min = min(cur_min, node.val)
        cur_max = max(cur_max, node.val)
        self.dfs(node.left, cur_min, cur_max)
        self.dfs(node.right, cur_min, cur_max)
        
        