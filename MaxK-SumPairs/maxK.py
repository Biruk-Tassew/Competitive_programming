class Solution:
    def maxOperations(nums: List[int], k: int) -> int:
        def mergeSort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                mergeSort(L)
                mergeSort(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
            return arr
        nums = list(filter(lambda a: a <= k, nums))
        nums = mergeSort(nums)
        count = 0
        i = 0
        j = len(nums)-1
        while i < j:
           
            if nums[i] + nums[j] == k:
                j -= 1
                i += 1
                count += 1
            elif  nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
            
        
        return count
