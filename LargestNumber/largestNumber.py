class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        outPut = ''
        maxNum = ''

        stringNums = [str(i) for i in nums]
        while stringNums:
            for i in stringNums:
                if not maxNum:
                    maxNum = i
                else:
                    if i + maxNum > maxNum + i:
                        maxNum = i

            outPut += maxNum
            stringNums.remove(maxNum)
            maxNum = ""
            
        if int(outPut[0]) == 0:
            outPut = "0"

        return "{outPut}".format(outPut = outPut)
        
