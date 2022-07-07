class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        for i in range(len(matrix)):
            if i < k:
                heapq.heappush(heap, (matrix[i][0], i, 0))
        
        for _ in range(k-1):
            val, row, col = heapq.heappop(heap)
            if col + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[row][col+1], row, col+1))
            
        return heap[0][0]
        
