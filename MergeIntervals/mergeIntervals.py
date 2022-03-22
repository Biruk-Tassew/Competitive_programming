class Solution:
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        def partitioning(start, end, arr):
            pivot = arr[end][0]
            j = start - 1
            for i in range(start, end):
                if(arr[i][0] <= pivot):
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[j+1], arr[end] = arr[end], arr[j+1]
            return j+1

        def quickSort(arr, start, end):
            if(start < end):
                pivotIndex = partitioning(start, end, arr)
                quickSort(arr, start, pivotIndex-1)
                quickSort(arr, pivotIndex + 1, end)
            return arr
        sortedIntervals = quickSort(intervals, 0, len(intervals)-1)
        outPut = []
        for i in sortedIntervals:
            newInterval = i
            if outPut:
                if outPut[-1][1] >= i[0]:
                    newInterval = outPut.pop()
                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]

            outPut.append(newInterval)

        return outPut
