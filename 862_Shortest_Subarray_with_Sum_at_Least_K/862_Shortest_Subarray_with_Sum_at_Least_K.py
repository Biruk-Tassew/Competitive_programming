class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        if k in nums:
            return 1
        
        comp = [0]*(len(nums) + 1)
        count = 1
        dQueue = collections.deque()
        outPut = len(nums) + 1
        
        while(count < len(comp)):
            comp[count] = comp[count-1] + nums[count-1]
            count += 1
        
        for i in range(len(comp)):
            while len(dQueue) > 0 and comp[i] - comp[dQueue[0]] >= k:
                outPut = min(outPut, i - dQueue.popleft())
            while len(dQueue) > 0 and comp[i] < comp[dQueue[-1]]:
                dQueue.pop()
            dQueue.append(i);
        
        if outPut != len(nums)+1:
            return outPut
        
        return -1
                

    
