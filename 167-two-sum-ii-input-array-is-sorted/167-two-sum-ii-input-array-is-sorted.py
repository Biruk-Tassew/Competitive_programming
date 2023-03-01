class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        for i in range(len(numbers)):
            
            diff = target-numbers[i]
            left = 0
            right = len(numbers)
            
            while left < right:
                
                mid = (left+right)//2
                
                if numbers[mid] > diff:
                    right = mid
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    if mid != i:
                        return [i+1, mid+1]
                    else:
                        if mid < len(numbers)-1 and numbers[mid+1] == diff:
                            return [i+1, mid+2]
       