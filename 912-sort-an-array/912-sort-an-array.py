class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        heapify(nums)
        
        while nums:
            ans.append(heappop(nums))
            
        return ans