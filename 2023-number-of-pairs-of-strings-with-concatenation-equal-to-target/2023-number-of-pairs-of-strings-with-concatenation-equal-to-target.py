class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                if i != j:
                    if nums[i] + nums[j] == target: 
                        count += 1
                    if  nums[j] + nums[i] == target:
                        count += 1
        return count