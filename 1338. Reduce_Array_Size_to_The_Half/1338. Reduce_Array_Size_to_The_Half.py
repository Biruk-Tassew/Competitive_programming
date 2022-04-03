class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if arr.count(arr[0])==len(arr):
            return 1
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

        arr.sort()
        compMap = dict()
        for i in arr:
            if i in compMap.keys():
                compMap[i] += 1
            else:
                compMap[i] = 1
        compArr = []
        for i in compMap.keys():
            compArr.append([compMap[i], i])

        
        sortedCompArr = countingSort(compArr)

        if sortedCompArr == compArr and sortedCompArr[-1] == sortedCompArr[0]:
            return len(sortedCompArr)//2
        if sortedCompArr[-1][0] >= len(arr)//2:
            return 1
        lastNum = sortedCompArr[-1][0]
        count = 1
        for i in range(len(sortedCompArr)-2, 1, -1):
            
            if lastNum < len(arr)//2:
                lastNum += sortedCompArr[i][0]
                count += 1
                
        
        return count
