# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        que = deque([root])
        res = []
        
        while que:
            layer_len = len(que)
            layer_nums = []
            for i in range(layer_len):
                node = que.popleft()
                layer_nums.append(node.val)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(sum(layer_nums)/len(layer_nums))
            
        return res
                
