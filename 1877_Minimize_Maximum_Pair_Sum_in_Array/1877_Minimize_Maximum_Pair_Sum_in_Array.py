class Solution:
    def minPairSum(self, nums: List[int]) -> int:
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
        nums=quickSort(nums, 0, len(nums)-1)
        maxNum = 0
        i = 0
        j = 1
        while i < len(nums):
            if nums[i] + nums[-j] > maxNum:
                maxNum = nums[i] + nums[-j]
            i += 1
            j += 1
        return maxNum
