class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        def partitioning(start, end, arr):
            pivot = arr[end]
            j = start - 1
            for i in range(start, end):
                if(arr[i] <= pivot):
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
        piles = quickSort(piles, 0, len(piles)-1)
        i = len(piles) - 2
        count = 0
        while i >= len(piles)/3:
            count += piles[i]
            i -= 2

        return count
        
