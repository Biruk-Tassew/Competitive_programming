class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        newArr = []
        count = [0]*101
        for i in nums:
            count[i] += 1;

        for i in range(1,101):
            count[i] = count[i-1] + count[i]
        for i in range(len(nums)):
            if nums[i] == 0:    
                newArr.append(0);
            else:
                newArr.append(count[nums[i]-1]);
        return newArr
        
