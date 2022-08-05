class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = 10**6
        
        while left <= right:
            mid = (right+left)//2
            count = 0
            
            for i in nums:
                count += i//mid
                if i%mid != 0:
                    count += 1
                
            if count <= threshold:
                right = mid - 1
            else:
                left = mid + 1
                
        return left
