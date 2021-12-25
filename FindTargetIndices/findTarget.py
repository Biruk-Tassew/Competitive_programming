class Solution(object):
    def targetIndices(self, nums, target):
        min_idx  = 0
        tempArr=[]
        for i in range(len(nums)-1):  
            min_idx = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_idx]: 
                    min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]; 
        count = 0   
        for i in nums: 
            if i == target:
                if count == 0:
                    tempArr.append(nums.index(i))
                    
                else:
                    tempArr.append(nums.index(i)+count)
                count += 1
            
        return tempArr
