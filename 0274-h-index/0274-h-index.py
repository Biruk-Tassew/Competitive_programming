class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        citations.sort()

        for i in range(len(citations)):
            if citations[i] >= size:
                return size

            size -= 1

        return size
        
# size = 5
# [3,0,6,1,5]


       
            
          
            