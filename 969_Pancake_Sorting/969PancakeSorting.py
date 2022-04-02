class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        outPut = []
        def flipArr(indx):
            for i in range(0, indx//2+1):
                arr[i], arr[indx-i] = arr[indx-i] ,arr[i]
        for i in range(len(arr)-1, 0, -1):
            for j in range(1, i+1):
                if arr[j] == i+1:
                    flipArr(j)
                    outPut.append(j+1)
                    break
            flipArr(i)
            outPut.append(i+1)
        return outPut
