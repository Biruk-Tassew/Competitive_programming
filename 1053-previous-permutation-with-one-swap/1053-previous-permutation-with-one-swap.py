class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        small = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                small = i
                
                for j in range(len(arr)-1, 0, -1):
                    if arr[j] != arr[j-1] and arr[j] < arr[small]:
                        arr[j], arr[small] = arr[small], arr[j]
                        
                        return arr
                
        return arr
                    
            