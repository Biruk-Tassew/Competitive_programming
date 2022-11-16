class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = ""
        count = 0
        
        for i in nums:
            if not count:
                ans = i
                
            if ans == i:
                count += 1
            else:
                count -= 1
                
        return ans 