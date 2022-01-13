class Solution(object):
    def sortColors(self, nums):
        mainPointer = 0
        secPointer = 0  
        target = 1
        arrLen = len(nums) - 1
        while mainPointer <= arrLen:
            if nums[mainPointer] > target:
                nums[mainPointer], nums[arrLen] = nums[arrLen], nums[mainPointer]
                arrLen -= 1
            elif nums[mainPointer] < target:
                nums[secPointer], nums[mainPointer] = nums[mainPointer], nums[secPointer]
                secPointer += 1
                mainPointer += 1
            else:
                mainPointer += 1
