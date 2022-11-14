class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        comp = len(nums)
        while right < comp:
            if nums[left] == nums[right]:
                cur_cnt = 1
                while right < len(nums) and nums[left] == nums[right]:
                    right += 1
                    cur_cnt += 1
                   
                diff = cur_cnt-2
                while cur_cnt > 2:
                    nums.remove(nums[left])
                    cur_cnt -= 1
                  
               
                left = right - diff
                right = left + 1 
                
            else:
                left = right
                right += 1
            comp = len(nums)
                
        print(nums)
        return len(nums)
                
                
                    