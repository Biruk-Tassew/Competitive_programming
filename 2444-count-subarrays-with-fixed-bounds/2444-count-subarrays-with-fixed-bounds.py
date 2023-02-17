class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        left = 0
        right = 0
        count = 0 
        left_flag = 0
        right_flag = 0
       
        
        
        while right < len(nums):
            while right < len(nums) and minK <= nums[right] <= maxK:
                
                if minK == nums[right]:
                    left_flag = right
                    
                if maxK == nums[right]:
                    right_flag = right
                    
                if minK == nums[left_flag] and maxK == nums[right_flag]:
                    count += min(left_flag - left, right_flag - left)+1
                        
                right += 1
            
            left = right+1
            left_flag = right
            right_flag = right
            right += 1
            
        return count 