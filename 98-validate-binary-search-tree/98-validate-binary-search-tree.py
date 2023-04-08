# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float('inf'), float('-inf'))
    def check(self, node, cur_max, cur_min):
        if not node:
            return True
        
        if node.val >= cur_max or node.val <= cur_min:
            return False
        
        left = self.check(node.left, min(cur_max, node.val), cur_min)
        right = self.check(node.right, cur_max, max(cur_min, node.val))
        
        return left and right