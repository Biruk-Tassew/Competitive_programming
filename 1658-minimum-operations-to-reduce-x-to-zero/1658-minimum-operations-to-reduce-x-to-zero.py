class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left_sum = sum(nums)-x
        if not left_sum:
            return len(nums)
        
        left = 0
        max_len = 0
        cur_sum = 0
        for right in range(len(nums)):
            
            cur_sum += nums[right]
            
            while left < right and  cur_sum > left_sum:
                cur_sum -= nums[left]
                left += 1
                
            if cur_sum == left_sum:
                max_len = max(max_len, right-left+1)
           
        if not max_len:
            return -1
        return len(nums)-max_len
            