class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        for i in range(len(numbers)):
            
            diff = target-numbers[i]
            left = i+1
            right = len(numbers)
            
            while left < right:
                
                mid = (left+right)//2
                
                if numbers[mid] > diff:
                    right = mid
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    return [i+1, mid+1]
       