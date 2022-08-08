# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, 0)]
        
        while stack:
            node, node_sum = stack.pop()
            node_sum += node.val
            
            if node.right:
                stack.append((node.right, node_sum))
            if node.left:
                stack.append((node.left, node_sum))
            elif not node.right:
                if node_sum == targetSum:
                    return True
                
        return False
            
            
