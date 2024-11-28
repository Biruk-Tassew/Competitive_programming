# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = defaultdict(list)
        que = deque([(root, 0)])
        min_idx = max_idx = 0
        level = 0

        while que:
            for _ in range(len(que)):
                node, idx = que.popleft()

                if node:
                    result[idx].append((level, node.val))

                    min_idx = min(min_idx, idx)
                    max_idx = max(max_idx, idx)

                    que.append((node.left, idx-1))
                    que.append((node.right, idx+1))

            level += 1

        result = [sorted(result[idx]) for idx in range(min_idx, max_idx+1)]
        return [[i[1] for i in j] for j in result]

