class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        reminders_count = [0]*k
        reminders_count[0] = 1
        running_sum = 0
        ans = 0
        
        for num in nums:
            running_sum = (running_sum+num)%k
            ans += reminders_count[running_sum]
            reminders_count[running_sum] += 1
            
            
        return ans
        