class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k) - self.solve(nums, k-1)
    
    def solve(self, nums, k):
        left = 0 
        right = 0
        
        seen = set()
        count = Counter()
        ans = 0
        
        while right < len(nums):
            
            seen.add(nums[right])
            count[nums[right]] += 1
            
            while len(seen) > k:
                count[nums[left]] -= 1
                
                if not count[nums[left]]:
                    seen.remove(nums[left])
                    
                left += 1
                
            ans += right-left+1
            right += 1
            
        return ans
                