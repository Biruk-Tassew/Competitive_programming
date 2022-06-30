class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         
        sum_dict = {}
        count = 0
        sum_dict[0] = 1
        sum_ = 0
        start = 0
        
        while start < len(nums):
            sum_ += nums[start]
            idx = sum_ - k
            if idx in sum_dict:
                count += sum_dict[idx]
                
            if sum_ in sum_dict:
                sum_dict[sum_] = sum_dict[sum_] + 1
            else:
                sum_dict[sum_] = 1
                
            start += 1
        return count
                    
                    
        
