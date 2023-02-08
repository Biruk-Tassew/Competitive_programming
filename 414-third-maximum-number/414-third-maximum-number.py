class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        seen = set()
        
        for num in nums:
            if num in seen:
                continue
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num
                
            seen.add(num)
                
        if third_max != float('-inf'):
            return third_max
        return max(nums)
                