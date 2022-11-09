class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        store = defaultdict(lambda :0)
        res = [0, 0]
        
        for i in nums:
            store[i] += 1
            if store[i] == 2:
                res[0] = i
         
        for i in range(1, len(nums)+1):
            if not store[i]:
                res[1] = i
                
        return res
            