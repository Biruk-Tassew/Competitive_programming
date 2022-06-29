class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        idx = 0
        zeros_count = 0
        length = 0
        max_count = 0
        
        while idx < len(nums):
            
            if not nums[idx]:
                zeros_count += 1
            
            while zeros_count > k:
                if not nums[length]:
                    zeros_count -= 1
                length += 1
            
            max_count = max(max_count, idx - length + 1)
            idx += 1
            
        
        return max_count
            
        
                        
                
            
        
