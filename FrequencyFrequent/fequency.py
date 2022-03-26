class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
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
        
        nums = mergeSort(nums)
        left = 0
        right = 0
        total = 0
        outPut = 0
        
        while right < len(nums):
            
            total += nums[right]
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
        
            outPut = max(outPut, right - left + 1)
            right += 1
            
        return outPut
