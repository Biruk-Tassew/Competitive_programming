class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = sorted(nums)
        return ans[len(ans)-k]