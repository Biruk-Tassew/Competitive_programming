class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = [] 
        minCapital = [] 

        for cap, pro in zip(capital , profits):
            minCapital.append((cap ,pro))

        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                cap , pro = heapq.heappop(minCapital)
                heapq.heappush(maxProfit , -1 * pro)
            
            if not maxProfit : break 

            w += -1 * heapq.heappop(maxProfit)

        return w