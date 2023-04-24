# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        que = deque([(root, 0)])
        max_len = 0
        
        while que:
            max_len = max(max_len, que[-1][1]-que[0][1]+1)
            for _ in range(len(que)):
                node, cur_w = que.popleft()
                
                if node.left:
                    que.append((node.left, cur_w *2))
                    
                if node.right:
                    que.append((node.right, cur_w*2 + 1))
                    
        return max_len