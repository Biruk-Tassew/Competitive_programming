class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        compMap = {}
        for i in words:
            if i in compMap:
                compMap[i] += 1
            else:
                compMap[i] = 1
        
        compArr = []
        for i in compMap:
            heapq.heappush(compArr, (-compMap[i],i))
                
        outPut = []     
        for i in range(k):
            outPut.append(heapq.heappop(compArr)[1])
            
        return outPut
