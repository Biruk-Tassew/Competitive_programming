class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
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
        count = collections.Counter(changed)
        outPut = []
        sortedArr = mergeSort(changed)
        for i in sorted(sortedArr):
            if count[i] == 0: 
                continue
            if count[2*i] == 0: 
                return []
            outPut += [i]
            if i == 0 and count[i] <= 1: 
                return []
            count[i] -= 1
            count[2*i] -= 1
        
        return outPut
