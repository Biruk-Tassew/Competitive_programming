# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_ = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
            if not (node.val % 2):
                if node.left:
                    if node.left.left:
                        sum_ += node.left.left.val
                    if node.left.right:
                        sum_ += node.left.right.val
                if node.right:
                    if node.right.right:
                        sum_ += node.right.right.val
                    if node.right.left:
                        sum_ += node.right.left.val
                        
        return sum_
