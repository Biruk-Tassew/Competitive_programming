class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        
        while left <= right:
            mid = (left+right)//2
            count = 0
            
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
            
