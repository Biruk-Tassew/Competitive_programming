class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations:
            return 0
        
        size = len(citations)
        citations = sorted(citations)
        
        if citations[0] >= size:
            return size
        
        for i in range(0, len(citations)):

            if size <= citations[i]:
                return size
            size -= 1
            
        return size
            
