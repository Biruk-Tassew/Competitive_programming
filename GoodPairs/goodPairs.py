class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        j = 1
        total = 0
        while i < len(nums)-1:
            while j < len(nums):
                if nums[i] == nums[j]:
                    total += 1
                j += 1
            i += 1
            j = i + 1
        return total
