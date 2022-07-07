class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        compMap = dict()
        for i in nums:
            if i in compMap:
                compMap[i] += 1
            else:
                compMap[i] = 1
            
        compArr = []
        for i in compMap:
            heapq.heappush(compArr,(compMap[i],i))
            if len(compArr)>k: 
                heapq.heappop(compArr)
        
        outPut = []     
        for i in compArr:
            outPut.append(i[1])
            
        return outPut
            
