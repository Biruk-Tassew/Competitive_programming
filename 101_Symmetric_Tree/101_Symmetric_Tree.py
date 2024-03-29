# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que = deque([(root.left, root.right)])
        
        while que:
            left, right = que.popleft()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            
            if left.val == right.val:
                que.append((left.left, right.right))
                que.append((left.right, right.left))
            else:
                return False
            
        return True
        
        
            
