# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        que, max_width = deque([(root, 0)]), 0
        while que:
            max_width = max(max_width, que[-1][1] - que[0][1])
            for _ in range(len(que)):
                node, cur_width = que.popleft()
                if node.left:
                    que.append((node.left, cur_width* 2 - 1))
                if node.right:
                    que.append((node.right, cur_width * 2))
        return max_width + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
