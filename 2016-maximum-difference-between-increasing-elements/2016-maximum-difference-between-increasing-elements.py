class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        max_num = float('-inf')
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if  nums[j] > nums[i]:
                    max_num = max(max_num, nums[j]-nums[i])
                
        if max_num != float('-inf'):
            return max_num
        return -1