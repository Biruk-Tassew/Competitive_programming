class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapify(heap)
        
        for _ in range(k):
            temp = - heappop(heap)
            remove = temp//2
            heappush(heap, -(temp-remove))
            
        return -sum(heap)