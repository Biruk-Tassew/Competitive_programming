class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        num_dict = {}
        odd_checker = [0]*len(nums)
        outPut = 0
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                odd_checker[i] = 1
        for i in range(1,len(nums)):
            odd_checker[i] += odd_checker[i-1]
            
        num_dict[0] = 1
        for i in range(len(nums)):
            if odd_checker[i] in num_dict:
                num_dict[odd_checker[i]] += 1
            else:
                num_dict[odd_checker[i]] = 1
                
            if odd_checker[i]-k in num_dict:
                outPut += num_dict[odd_checker[i]-k]
        return outPut
