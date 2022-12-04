class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        
        for i in range(1, n//2 + 1):
            if not n%i:
                if n//i == i:
                    count += 1
                else:
                    count += 2
                
            if count > 3:
                return False
            
        return count == 3
                