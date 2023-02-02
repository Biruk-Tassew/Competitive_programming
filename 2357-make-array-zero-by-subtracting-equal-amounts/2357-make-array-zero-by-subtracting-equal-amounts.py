class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        heapify(nums)
        count = 0
        while sum(nums):
            if nums[0]:
                min_num = nums[0]
                nums = [num - min_num for num in nums]
                count += 1
            else:
                heappop(nums)
            
                    
        return count