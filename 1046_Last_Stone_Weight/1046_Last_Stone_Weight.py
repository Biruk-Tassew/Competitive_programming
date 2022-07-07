class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        
        for i in stones:
            heapq.heappush(heap, -i)
            
        while len(heap) >= 2:
            stone_one = heapq.heappop(heap)
            stone_two = heapq.heappop(heap)
            
            if stone_one != stone_two:
                heapq.heappush(heap, stone_one-stone_two)
                
        if heap:
            return -heap[-1]
        return 0
                
        
