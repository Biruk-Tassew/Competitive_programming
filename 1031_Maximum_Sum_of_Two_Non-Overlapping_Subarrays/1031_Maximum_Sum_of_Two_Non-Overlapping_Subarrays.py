class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.max_(nums, firstLen, secondLen), self.max_(nums, secondLen, firstLen))
        
    def max_(self, nums, firstLen, secondLen):
        idx = 0
        max_w1 = 0
        max_w2 = 0
        temp_sum_w1 = 0
        temp_sum_w2 = 0
        
        while idx < firstLen+secondLen:
            if idx < firstLen:
                temp_sum_w1 += nums[idx]
            else:
                temp_sum_w2 += nums[idx]
                
            idx += 1
        
        idx = firstLen+secondLen
        outPut = temp_sum_w1 + temp_sum_w2
        max_w1 = temp_sum_w1
        
        while idx < len(nums):
            temp_sum_w1 += nums[idx-secondLen] - nums[idx-firstLen-secondLen]
            temp_sum_w2 += nums[idx] - nums[idx-secondLen]
            max_w1 = max(max_w1, temp_sum_w1)
            outPut = max(outPut, max_w1+temp_sum_w2)
            idx += 1
            
        return outPut
