class Solution(object):
    def sortSentence(self, s):
        tempArr = s.split(" ")
        tempArr2 = []
        newArr = ["tmp0"]*len(tempArr)
        temp = 0
        while int(newArr[-1][-1]) < len(tempArr):
            for i in range(len(tempArr)):
                if int(tempArr[i][-1]) == temp+1:
                    newArr[temp] = tempArr[i]
                    temp += 1
        for i in newArr:
            tempArr2.append(i[:-1])
        newstr = " "
        newstr = newstr.join(tempArr2)
        return newstr
