# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        cur_path = []
        paths = set()
        self.findPaths(root, cur_path, paths)
        return paths
    def findPaths(self, node, cur_path, paths):
        if not node:
            return 
        if not node.left and not node.right:
            cur_path.append(str(node.val))
            paths.add("->".join(cur_path[:]))
            cur_path.pop()
            return
        
        
        cur_path.append(str(node.val))    
        self.findPaths(node.left, cur_path, paths)
        self.findPaths(node.right, cur_path, paths)
        
        cur_path.pop()       