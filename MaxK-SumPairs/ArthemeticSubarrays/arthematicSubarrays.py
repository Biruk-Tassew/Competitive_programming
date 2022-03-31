class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def devider(nums: List[int], start, end):
            nums = nums[start: end+1]
            return nums
        def mainLogic(nums: List[int]):
            nums.sort()
            outPut = []
            i =0
            while i < len(nums)-1:
                outPut.append(nums[i+1]-nums[i])
                i += 1
            return outPut
        idx = 0
        outPut = []
        boolOutPut = []
        while idx < len(l):
            newNums = devider(nums, l[idx], r[idx])
            newNums = mainLogic(newNums)
            outPut.append(newNums)
            idx += 1
        for i in outPut:
            result = i.count(i[0]) == len(i)
            if result:
                boolOutPut.append(True)
            else:
                boolOutPut.append(False)

        return boolOutPut
