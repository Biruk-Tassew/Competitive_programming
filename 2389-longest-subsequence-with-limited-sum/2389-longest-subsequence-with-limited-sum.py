class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        ans = []
        for query in queries:
                
            left = 0
            right = len(nums)-1
            
            while left <= right:
                mid = (left+right)//2
                
                if nums[mid] > query:
                    right = mid - 1 
                else:
                    left = mid + 1
               
            
            ans.append(left)
            
        return ans