# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.levels = defaultdict(int)
        self.max_depth = defaultdict(int)
        self.first_largest = defaultdict(int)
        self.second_largest = defaultdict(int)
        
        self.dfs(root, 0)
        res = []
        for query in queries:
            if self.first_largest[self.levels[query]] == self.max_depth[query]:
                res.append(self.levels[query] + self.second_largest[self.levels[query]] - 1)
            else:
                res.append(self.levels[query] + self.first_largest[self.levels[query]] - 1)
                
        return res
        
    def dfs(self, node, cur_lvl):
        if not node:
            return 0
        
        self.levels[node.val] = cur_lvl
        self.max_depth[node.val] = 1+max(self.dfs(node.left, cur_lvl+1), self.dfs(node.right, cur_lvl+1)) 
        
        if self.first_largest[cur_lvl] < self.max_depth[node.val]:
            self.second_largest[cur_lvl] = self.first_largest[cur_lvl]
            self.first_largest[cur_lvl] = self.max_depth[node.val]
        elif self.second_largest[cur_lvl] < self.max_depth[node.val]:
            self.second_largest[cur_lvl] = self.max_depth[node.val]
            
        return self.max_depth[node.val]