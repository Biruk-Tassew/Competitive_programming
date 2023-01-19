class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        running_sum = 0
        count = [1] + [0] * k
        
        for num in nums:
            running_sum = (running_sum + num) % k
            ans += count[running_sum]
            count[running_sum] += 1
        
        return ans
        
        