class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        windowSize = []
        incQueue = deque()
        dicQueue = deque()
        
        incQueue.append(nums[0])
        dicQueue.append(nums[0])
        
        res = 1
        count = 0
    
        for i in range(1, len(nums)):
            
            while incQueue and incQueue[-1] > nums[i]:
                incQueue.pop()
                
            while dicQueue and dicQueue[-1] < nums[i]:
                dicQueue.pop()  
                
            incQueue.append(nums[i])
            dicQueue.append(nums[i])
            
            while dicQueue[0] - incQueue[0] > limit:
                if incQueue[0] == nums[count]:
                    incQueue.popleft()
                if dicQueue[0] == nums[count]:
                    dicQueue.popleft()
                count += 1
            res = max(res, i - count + 1)
        return res
        
                
