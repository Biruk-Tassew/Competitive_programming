class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10**9
        
        while left < right:
            mid = (left+right)//2
            
            if self.decide(piles, mid, h):
                right = mid
            else:
                left = mid + 1
                
        return left
            
    def decide(self, nums, k, hr):
        cur_hr = 0
        for num in nums:
            cur_hr += ceil(num/k)
            
            if cur_hr > hr:
                return False
            
        return True