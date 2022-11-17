class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
                
            left = i+1
            right = len(nums)-1
            
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                
                if not sum_3:
                    res.append((nums[i], nums[left], nums[right]))
                    
                    left_val = nums[left]
                    right_val = nums[right]
                    while left < right and nums[right] == right_val:
                        right -= 1
                    while left < right and nums[left] == left_val:
                        left += 1
                elif sum_3 > 0:
                    right -= 1
                else:
                    left += 1
                    
        return res 
                    
            