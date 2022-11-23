# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.post_height = defaultdict(int)
        self.pre_height = defaultdict(int)
        self.max_height = 0
        self.pre_dfs(root, 0)
        self.max_height = 0
        self.post_dfs(root, 0)
        
        res = []
        for query in queries:
            res.append(max(self.post_height[query], self.pre_height[query]))
                
        return res
        
    def post_dfs(self, node, cur_lvl):
        if not node:
            return 0
        
        
        self.post_height[node.val] = self.max_height
        self.max_height = max(self.max_height, cur_lvl)
        self.post_dfs(node.right, cur_lvl+1)
        self.post_dfs(node.left, cur_lvl+1)
        
        
    def pre_dfs(self, node, cur_lvl):
        if not node:
            return 0
        
        self.pre_height[node.val] = self.max_height
        self.max_height = max(self.max_height, cur_lvl)
        self.pre_dfs(node.left, cur_lvl+1)
        self.pre_dfs(node.right, cur_lvl+1)