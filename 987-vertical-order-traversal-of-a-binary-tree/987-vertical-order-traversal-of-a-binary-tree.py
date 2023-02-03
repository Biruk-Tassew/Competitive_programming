# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que = deque([(root, 0, 0)])
        ans = defaultdict(list)
        
        while que:
            node, x_pos, y_pos = que.popleft()
            ans[y_pos].append((x_pos, node.val))
            
            if node.left:
                que.append((node.left, x_pos+1, y_pos-1))
            if node.right:
                que.append((node.right, x_pos+1, y_pos+1))
        
        sorted_by_y = sorted(ans.items())
        ans = []
        for y_pos, node in sorted_by_y:
            n_arr = []
            for _, node_val in sorted(node):
                n_arr.append(node_val)
                
            ans.append(n_arr)
            
        return ans