# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        return self.dfs(root1)==self.dfs(root2)
    
    def dfs(self, node):
        res = []
        stack = [node]
        while stack: 
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            elif not node.left:
                res.append(node.val)
            
        return res