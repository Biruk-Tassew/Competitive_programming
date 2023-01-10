# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que_p = deque([p])
        que_q = deque([q])
        
        while que_q or que_p:
            p_level = []
            q_level = []
            for _ in range(len(que_p)):
                node = que_p.popleft()
                
                if not node:
                    p_level.append(node)
                    continue
                    
                p_level.append(node.val)
                que_p.append(node.left)
                que_p.append(node.right)
                    
            for _ in range(len(que_q)):
                node = que_q.popleft()
                
                if not node:
                    q_level.append(node)
                    continue
                    
                q_level.append(node.val)
                que_q.append(node.left)
                que_q.append(node.right)
              
            
            if p_level != q_level:
                return False
            
        return True
                