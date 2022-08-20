# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        que = deque([root])
        ans = []
        layer_no = 0
        
        while que:
            layer = []
            for i in range(len(que)):
                node = que.popleft()
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
                if layer_no % 2:
                    layer.insert(0, node.val)
                else:
                     layer.append(node.val)
            ans.append(layer)
            layer_no += 1
            
        return ans
