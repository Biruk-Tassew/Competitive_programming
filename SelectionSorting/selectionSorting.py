class Solution: 
    def select(self, arr, i):
        pass
    def selectionSort(self, arr,n):
        min_idx  = 0
        for i in range(n-1):  
            min_idx = i
            for j in range(i+1,n):
                if arr[j] < arr[min_idx]: 
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]; 
            
        return arr
