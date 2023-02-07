class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapify(nums)
        
        n= len(nums)-k
        while n:
            heappop(nums)
            n -= 1
            
        return heappop(nums)