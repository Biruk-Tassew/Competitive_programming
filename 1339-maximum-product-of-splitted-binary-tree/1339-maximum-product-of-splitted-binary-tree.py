# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.cur_max = 0
        self.total = 0
        self.total = self.dfs(root)
        self.dfs(root)
        return self.cur_max % (10**9 + 7)
        
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.cur_max = max(self.cur_max, left*(self.total-left), right*(self.total-right))
        return left + right + node.val