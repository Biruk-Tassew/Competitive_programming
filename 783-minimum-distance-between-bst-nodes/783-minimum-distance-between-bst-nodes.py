# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        que = deque([root])
        nums = []
        
        while que:
            node = que.popleft()
            nums.append(node.val)
            
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        min_ = float('inf')
        for j in range(len(nums)-1):
            min_ = min(min_, nums[j+1]-nums[j])
            
        return min_
                