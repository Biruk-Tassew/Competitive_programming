class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def countingSort(arr):
            newArr = [0] * 1000
            lastArr = [0] * len(arr)
            for i in arr:
                newArr[i[0]] += 1
            for j in range(len(newArr)-1):
                newArr[j+1] = newArr[j] + newArr[j+1]
            i = len(arr) - 1
            while i >= 0:
                lastArr[newArr[arr[i][0]]-1] = arr[i]
                newArr[arr[i][0]] -= 1
                i -= 1
            return lastArr

        nums.sort()
        compMap = dict()
        for i in nums:
            if i in compMap.keys():
                compMap[i] += 1
            else:
                compMap[i] = 1
        compArr = []
        for i in compMap.keys():
            compArr.append([compMap[i], i])

        
        sortedCompArr = countingSort(compArr)
        outPut = []
        
        i = -1
        while -i <= k:
            outPut.append(sortedCompArr[i][1])
            i -= 1
        return outPut
