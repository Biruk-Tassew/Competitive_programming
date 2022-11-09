class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        uni_sum = sum(set(nums))
        given_sum = sum(nums)
        whole_sum = len(nums)*(len(nums)+1)//2
        
        return [given_sum-uni_sum, whole_sum-uni_sum]
            